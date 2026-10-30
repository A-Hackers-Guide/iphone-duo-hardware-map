# `_UIViewGlass`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewMaterial`
- 1 instance variables, 23 properties, 63 instance methods, 1 class methods

## Instance variables

```
_underlyingMaterial;
```

## Properties

```
@property (Tq,N,R) variant;
@property (Tq,N,R) size;
@property (Tq,N) identifier;
@property (Td,N) smoothness;
@property (T@"UIColor",N,&) tintColor;
@property (T@"UIColor",N,&) controlTintColor;
@property (T@"NSString",N,C) subvariant;
@property (TB,N) contentLensing;
@property (TB,N) highlightsDisplayAngle;
@property (TB,N) excludingPlatter;
@property (TB,N) excludingForeground;
@property (TB,N) excludingShadow;
@property (TB,N) excludingControlLensing;
@property (TB,N) excludingControlDisplacement;
@property (TB,N) flexible;
@property (Tq,N) _flexVariant;
@property (TB,N) _enabledWithoutSolarium;
@property (TB,N) boostWhitePoint;
@property (TB,N) allowsGrouping;
@property (T@"NSString",N,C) backdropGroupName;
@property (T@"NSString",N,C) debugIdentifier;
@property (TB,N) intelligence;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[_UIViewGlass systemTintAmount];
```

## Instance methods

```
-[_UIViewGlass smoothness];
-[_UIViewGlass setSmoothness:];
-[_UIViewGlass setDebugIdentifier:];
-[_UIViewGlass _setEnabledWithoutSolarium:];
-[_UIViewGlass setAdaptiveInitialLuminance:];
-[_UIViewGlass debugIdentifier];
-[_UIViewGlass setAdaptiveFixedLuminance:];
-[_UIViewGlass intelligence];
-[_UIViewGlass identifier];
-[_UIViewGlass init];
-[_UIViewGlass initWithVariant:];
-[_UIViewGlass setHighlightsDisplayAngle:];
-[_UIViewGlass setFlexible:];
-[_UIViewGlass excludingPlatter];
-[_UIViewGlass backdropGroupName];
-[_UIViewGlass setBoostWhitePoint:];
-[_UIViewGlass _flexVariant];
-[_UIViewGlass initWithVariant:size:smoothness:];
-[_UIViewGlass boostWhitePoint];
-[_UIViewGlass setAdaptiveStyle:];
-[_UIViewGlass flexible];
-[_UIViewGlass setBackdropGroupName:];
-[_UIViewGlass initWithVariant:size:smoothness:state:];
-[_UIViewGlass setSubvariant:];
-[_UIViewGlass size];
-[_UIViewGlass _setFlexVariant:];
-[_UIViewGlass setIdentifier:];
-[_UIViewGlass setExcludingControlLensing:];
-[_UIViewGlass initWithVariant:size:];
-[_UIViewGlass setExcludingShadow:];
-[_UIViewGlass _resolvedMaterialUsingTraitCollection:size:];
-[_UIViewGlass setTintColor:];
-[_UIViewGlass setAdaptive:];
-[_UIViewGlass highlightsDisplayAngle];
-[_UIViewGlass excludingForeground];
-[_UIViewGlass _identityGlass];
-[_UIViewGlass initWithVariant:size:state:];
-[_UIViewGlass _enabledWithoutSolarium];
-[_UIViewGlass setFixedBackgroundColor:];
-[_UIViewGlass initWithVariant:smoothness:state:];
-[_UIViewGlass setAllowsGrouping:];
-[_UIViewGlass contentLensing];
-[_UIViewGlass description];
-[_UIViewGlass tintColor];
-[_UIViewGlass allowsGrouping];
-[_UIViewGlass setSharpTinting:];
-[_UIViewGlass controlTintColor];
-[_UIViewGlass excludingControlLensing];
-[_UIViewGlass setControlTintColor:];
-[_UIViewGlass initWithVariant:size:smoothness:subdued:];
-[_UIViewGlass setExcludingControlDisplacement:];
-[_UIViewGlass setContentLensing:];
-[_UIViewGlass setExcludingPlatter:];
-[_UIViewGlass initWithVariant:smoothness:];
-[_UIViewGlass isEqual:];
-[_UIViewGlass initWithVariant:state:];
-[_UIViewGlass setIntelligence:];
-[_UIViewGlass subvariant];
-[_UIViewGlass setMeshed:];
-[_UIViewGlass excludingControlDisplacement];
-[_UIViewGlass setExcludingForeground:];
-[_UIViewGlass variant];
-[_UIViewGlass excludingShadow];
```
