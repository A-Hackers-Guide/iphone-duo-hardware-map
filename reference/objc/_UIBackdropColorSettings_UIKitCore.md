# `_UIBackdropColorSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _hasObservedValues;
@"_UIBackdropViewSettings" _parentSettings;
```

## Properties

```
@property (T@"_UIBackdropViewSettings",N,V_parentSettings) parentSettings;
@property (TB,N,V_hasObservedValues) hasObservedValues;
@property (Td,N) averageHue;
@property (Td,N) averageSaturation;
@property (Td,N) averageBrightness;
@property (Td,N) contrast;
@property (T@"UIColor",R,N) color;
```

## Instance methods

```
-[_UIBackdropColorSettings setContrast:];
-[_UIBackdropColorSettings averageSaturation];
-[_UIBackdropColorSettings parentSettings];
-[_UIBackdropColorSettings color];
-[_UIBackdropColorSettings setDefaultValues];
-[_UIBackdropColorSettings contrast];
-[_UIBackdropColorSettings applyCABackdropLayerStatistics:];
-[_UIBackdropColorSettings averageBrightness];
-[_UIBackdropColorSettings averageHue];
-[_UIBackdropColorSettings hasObservedValues];
-[_UIBackdropColorSettings setAverageBrightness:];
-[_UIBackdropColorSettings setAverageHue:];
-[_UIBackdropColorSettings setAverageSaturation:];
-[_UIBackdropColorSettings setHasObservedValues:];
-[_UIBackdropColorSettings setParentSettings:];
-[_UIBackdropColorSettings setValuesFromModel:];
```
