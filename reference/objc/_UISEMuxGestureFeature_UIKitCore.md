# `_UISEMuxGestureFeature`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISEGestureFeature`
- Protocols: `_UISEGestureFeatureDelegate`
- 5 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<_UISEGestureFeatureSettings>" _settings;
@? _createFeatureBlock;
@"NSMutableDictionary" _subfeatures;
Q _fails;
Q _recognizes;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_subfeatures) subfeatures;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISEMuxGestureFeature featureDidChangeState:];
-[_UISEMuxGestureFeature _incorporateSample:];
-[_UISEMuxGestureFeature subfeatures];
-[_UISEMuxGestureFeature debugDictionary];
-[_UISEMuxGestureFeature initWithSettings:createFeatureBlock:];
```
