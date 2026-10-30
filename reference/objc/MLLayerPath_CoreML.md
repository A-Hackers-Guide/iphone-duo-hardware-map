# `MLLayerPath`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _scopedModelNames;
@"NSString" _layerName;
```

## Properties

```
@property (T@"NSString",C,N,V_layerName) layerName;
@property (T@"NSArray",C,N,V_scopedModelNames) scopedModelNames;
```

## Instance methods

```
-[MLLayerPath init];
-[MLLayerPath scopedModelNames];
-[MLLayerPath isEqualToMLLayerPath:];
-[MLLayerPath layerName];
-[MLLayerPath appendPathComponent:];
-[MLLayerPath hash];
-[MLLayerPath setScopedModelNames:];
-[MLLayerPath copyWithZone:];
-[MLLayerPath initWithScopedModelAndLayerName:layerName:];
-[MLLayerPath isEqual:];
-[MLLayerPath setLayerName:];
```
