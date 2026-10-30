# `UIDynamicItemBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 12 instance variables, 9 properties, 44 instance methods, 1 class methods

## Instance variables

```
B _useDefaultViewPropertiesApplier;
{?="elasticityChanged"b1"frictionChanged"b1"densityChanged"b1"resistanceChanged"b1"angularResistanceChanged"b1"rotationEnabledChanged"b1"useDefaultViewPropertiesApplierChanged"b1"chargeChanged"b1"dynamicChanged"b1} _stateFlags;
@"NSMapTable" _cachedAngularVelocities;
@"NSMapTable" _cachedLinearVelocities;
B _anchored;
B _allowsRotation;
d _elasticity;
d _friction;
d _density;
d _resistance;
d _angularResistance;
d _charge;
```

## Properties

```
@property (T@"NSArray",R,C,N) items;
@property (Td,N,V_elasticity) elasticity;
@property (Td,N,V_friction) friction;
@property (Td,N,V_density) density;
@property (Td,N,V_resistance) resistance;
@property (Td,N,V_angularResistance) angularResistance;
@property (Td,N,V_charge) charge;
@property (TB,N,GisAnchored,V_anchored) anchored;
@property (TB,N,V_allowsRotation) allowsRotation;
```

## Class methods

```
+[UIDynamicItemBehavior _isPrimitiveBehavior];
```

## Instance methods

```
-[UIDynamicItemBehavior setFriction:];
-[UIDynamicItemBehavior friction];
-[UIDynamicItemBehavior charge];
-[UIDynamicItemBehavior init];
-[UIDynamicItemBehavior density];
-[UIDynamicItemBehavior items];
-[UIDynamicItemBehavior removeItem:];
-[UIDynamicItemBehavior setCharge:];
-[UIDynamicItemBehavior addItem:];
-[UIDynamicItemBehavior description];
-[UIDynamicItemBehavior setDensity:];
-[UIDynamicItemBehavior initWithItems:];
-[UIDynamicItemBehavior useDefaultViewPropertiesApplier];
-[UIDynamicItemBehavior _angleForItem:];
-[UIDynamicItemBehavior _angularResistanceForItem:];
-[UIDynamicItemBehavior _associate];
-[UIDynamicItemBehavior _configureBody:forView:];
-[UIDynamicItemBehavior _densityForItem:];
-[UIDynamicItemBehavior _dissociate];
-[UIDynamicItemBehavior _elasticityForItem:];
-[UIDynamicItemBehavior _frictionForItem:];
-[UIDynamicItemBehavior _massForItem:];
-[UIDynamicItemBehavior _positionForItem:];
-[UIDynamicItemBehavior _reevaluate:];
-[UIDynamicItemBehavior _resistanceForItem:];
-[UIDynamicItemBehavior _rotationEnabledForItem:];
-[UIDynamicItemBehavior _setAngle:forItem:];
-[UIDynamicItemBehavior _setPosition:forItem:];
-[UIDynamicItemBehavior addAngularVelocity:forItem:];
-[UIDynamicItemBehavior addLinearVelocity:forItem:];
-[UIDynamicItemBehavior allowsRotation];
-[UIDynamicItemBehavior angularResistance];
-[UIDynamicItemBehavior angularVelocityForItem:];
-[UIDynamicItemBehavior applyImpulse:toItem:];
-[UIDynamicItemBehavior elasticity];
-[UIDynamicItemBehavior isAnchored];
-[UIDynamicItemBehavior linearVelocityForItem:];
-[UIDynamicItemBehavior resistance];
-[UIDynamicItemBehavior setAllowsRotation:];
-[UIDynamicItemBehavior setAnchored:];
-[UIDynamicItemBehavior setAngularResistance:];
-[UIDynamicItemBehavior setElasticity:];
-[UIDynamicItemBehavior setResistance:];
-[UIDynamicItemBehavior setUseDefaultViewPropertiesApplier:];
```
