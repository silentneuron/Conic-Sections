#Conic Section


An interactive Python visualization showing how different conic sections — **circle**, **ellipse**, **parabola**, and **hyperbola** — are formed when a **plane cuts a double cone**.

---

##  Features
-  3D cone + plane visualization  
-  Dynamic 2D conic section plot  
-  Adjustable sliders for:
  - `alpha` → cone’s half-angle  
  - `beta` → plane’s inclination angle  
-  Visual understanding of conic geometry  

---

##  How It Works

| Case | Condition | Result |
|------|------------|---------|
| β < α | Plane cuts cone at an angle smaller than cone | **Ellipse** |
| β = α | Plane parallel to cone generator | **Parabola** |
| β > α | Plane steeper than cone | **Hyperbola** |
| β = 0 | Plane perpendicular to cone axis | **Circle** |

---

## Requirements
```bash
pip install numpy matplotlib ipywidgets
