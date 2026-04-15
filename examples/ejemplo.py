"""
ejemplo.py
==========
Script de ejemplo de firstact.
Demuestra los calculos principales de la libreria.
"""

from firstact import MortalityTable, Insurance, Annuity, Premium
from firstact.utils import to_cont

print("=" * 55)
print("  firstact — Ejemplo de uso")
print("=" * 55)

# Cargar tabla
t = MortalityTable.ilt()
print(f"\nTabla cargada: {t}")

# Funciones biometricas
print("\n--- Funciones biometricas (x=35) ---")
print(f"  lx(35) = {t.lx(35):,.0f}")
print(f"  qx(35) = {t.qx(35):.5f}")
print(f"  px(35) = {t.px(35):.5f}")
print(f"  10p35  = {t.npx(10, 35):.5f}")
print(f"  ex(35) = {t.ex(35):.4f}")

# Seguros
ins = Insurance(t, i=0.06)
print("\n--- Seguros (x=35, i=6%) ---")
print(f"  A_35              = {ins.Ax(35):.5f}")
print(f"  A^1_{{35:20|}}   = {ins.Ax_temporal(35, 20):.5f}")
print(f"  20E_35            = {ins.nEx(35, 20):.5f}")
print(f"  A_{{35:20|}}     = {ins.Ax_dotal_mixto(35, 20):.5f}")

# Anualidades
ann = Annuity(t, i=0.06)
print("\n--- Anualidades (x=35, i=6%) ---")
print(f"  a-dot_35          = {ann.ax(35):.4f}")
print(f"  a-dot_{{35:20|}} = {ann.ax_temp(35, 20):.4f}")

# Primas y reservas
pre = Premium(t, i=0.06)
print("\n--- Primas y Reservas (x=35, n=20, i=6%) ---")
P = pre.prima_vida_entera(35)
print(f"  P vida entera     = {P:.6f}")
print(f"  P temporal 20a    = {pre.prima_temporal(35, 20):.6f}")
print(f"  P dotal mixto 20a = {pre.prima_dotal_mixto(35, 20):.6f}")
print(f"  10V vida entera   = {pre.reserva_vida_entera(35, 10):.6f}")

# Conversiones
print("\n--- Conversiones discreto -> continuo (UDD) ---")
Ax_bar = to_cont(ins.Ax(35), i=0.06, kind='seguro')
ax_bar = to_cont(ann.ax(35), i=0.06, kind='anualidad')
print(f"  A_35 -> A-bar_35  = {Ax_bar:.5f}")
print(f"  a-dot_35 -> a-bar_35 = {ax_bar:.4f}")

# Caso practico
print("\n--- Caso Practico: Dotal mixto x=30, n=25, SA=$1,000,000 ---")
SA = 1_000_000
P_anual = pre.prima_dotal_mixto(30, 25) * SA
P_mens  = pre.prima_fraccionada(P_anual, m=12)
R10     = pre.reserva_dotal_mixto(30, 25, t=10) * SA
print(f"  Prima anual   = ${P_anual:>12,.2f}")
print(f"  Prima mensual = ${P_mens:>12,.2f}")
print(f"  Reserva t=10  = ${R10:>12,.2f}")

print("\n" + "=" * 55)
print("  Ejemplo completado exitosamente!")
print("=" * 55)
