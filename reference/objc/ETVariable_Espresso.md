# `ETVariable`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
f _initializationAlpha;
f _initializationBeta;
Q _kind;
@"NSString" _name;
@"NSString" _layerName;
Q _initializationMode;
@"ETModelDef" _model;
```

## Properties

```
@property (T@"ETModelDef",W,N,V_model) model;
@property (TQ,N,V_kind) kind;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_layerName) layerName;
@property (TQ,V_initializationMode) initializationMode;
@property (Tf,V_initializationAlpha) initializationAlpha;
@property (Tf,V_initializationBeta) initializationBeta;
```

## Instance methods

```
-[ETVariable model];
-[ETVariable setKind:];
-[ETVariable updateWithData:];
-[ETVariable setModel:];
-[ETVariable copyData];
-[ETVariable layerName];
-[ETVariable setName:];
-[ETVariable name];
-[ETVariable kind];
-[ETVariable setLayerName:];
-[ETVariable getOpaqueCopy];
-[ETVariable initWithModelDef:];
-[ETVariable initializationAlpha];
-[ETVariable initializationBeta];
-[ETVariable initializationMode];
-[ETVariable setInitializationAlpha:];
-[ETVariable setInitializationBeta:];
-[ETVariable setInitializationMode:];
-[ETVariable swapWithOpaqueCopy:];
```
