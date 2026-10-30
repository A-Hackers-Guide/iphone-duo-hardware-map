# `ETOptimizerDefSGD`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ETOptimizerDef`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
f _lr;
f _lr_decay_epoch;
f _momentum;
f _weight_decay;
```

## Properties

```
@property (Tf,V_lr) lr;
@property (Tf,V_lr_decay_epoch) lr_decay_epoch;
@property (Tf,V_momentum) momentum;
@property (Tf,V_weight_decay) weight_decay;
```

## Instance methods

```
-[ETOptimizerDefSGD init];
-[ETOptimizerDefSGD momentum];
-[ETOptimizerDefSGD setMomentum:];
-[ETOptimizerDefSGD lr];
-[ETOptimizerDefSGD lr_decay_epoch];
-[ETOptimizerDefSGD setLr:];
-[ETOptimizerDefSGD setLr_decay_epoch:];
-[ETOptimizerDefSGD setWeight_decay:];
-[ETOptimizerDefSGD weight_decay];
```
