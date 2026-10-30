# `_UIButtonConfigurationStyleBehaviors`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 30 instance methods, 16 class methods

## Instance variables

```
q _style;
@"NSString" _styleDescription;
@? _calculateForegroundColor;
@? _calculateBackgroundColor;
@? _calculateBackgroundVisualEffect;
@? _calculateMaterial;
@? _calculateMonochromaticTreatment;
q _selectionStyle;
q _automaticMacIdiomStyle;
q _cornerStyle;
q _contentMaterialRenderingMode;
```

## Properties

```
@property (Tq,R,N,V_style) style;
@property (T@"NSString",C,N,V_styleDescription) styleDescription;
@property (T@?,C,N,V_calculateForegroundColor) calculateForegroundColor;
@property (T@?,C,N,V_calculateBackgroundColor) calculateBackgroundColor;
@property (T@?,C,N,V_calculateBackgroundVisualEffect) calculateBackgroundVisualEffect;
@property (T@?,C,N,V_calculateMaterial) calculateMaterial;
@property (T@?,C,N,V_calculateMonochromaticTreatment) calculateMonochromaticTreatment;
@property (Tq,N,V_selectionStyle) selectionStyle;
@property (Tq,N,V_automaticMacIdiomStyle) automaticMacIdiomStyle;
@property (Tq,N,V_cornerStyle) cornerStyle;
@property (Tq,N,V_contentMaterialRenderingMode) contentMaterialRenderingMode;
```

## Class methods

```
+[_UIButtonConfigurationStyleBehaviors glassMonochromaticTreatmentFromBaseColor:traitCollection:];
+[_UIButtonConfigurationStyleBehaviors homescreenCloseGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors tintBehaviors];
+[_UIButtonConfigurationStyleBehaviors glassBehaviors];
+[_UIButtonConfigurationStyleBehaviors fillBehaviors];
+[_UIButtonConfigurationStyleBehaviors posterSwitcherGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors grayBehaviors];
+[_UIButtonConfigurationStyleBehaviors controlCenterGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors tintedGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors sidebarGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors emptyBehaviors];
+[_UIButtonConfigurationStyleBehaviors plainBehaviors:];
+[_UIButtonConfigurationStyleBehaviors prominentClearGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors behaviorForStyle:];
+[_UIButtonConfigurationStyleBehaviors clearGlassBehaviors];
+[_UIButtonConfigurationStyleBehaviors avPlayerGlassBehaviors];
```

## Instance methods

```
-[_UIButtonConfigurationStyleBehaviors cornerStyle];
-[_UIButtonConfigurationStyleBehaviors contentMaterialRenderingMode];
-[_UIButtonConfigurationStyleBehaviors setCalculateMaterial:];
-[_UIButtonConfigurationStyleBehaviors calculateMaterial];
-[_UIButtonConfigurationStyleBehaviors setCalculateForegroundColor:];
-[_UIButtonConfigurationStyleBehaviors setCornerStyle:];
-[_UIButtonConfigurationStyleBehaviors setSelectionStyle:];
-[_UIButtonConfigurationStyleBehaviors setCalculateBackgroundVisualEffect:];
-[_UIButtonConfigurationStyleBehaviors selectionStyle];
-[_UIButtonConfigurationStyleBehaviors initWithStyle:];
-[_UIButtonConfigurationStyleBehaviors style];
-[_UIButtonConfigurationStyleBehaviors setContentMaterialRenderingMode:];
-[_UIButtonConfigurationStyleBehaviors behaviorForState:];
-[_UIButtonConfigurationStyleBehaviors setAutomaticMacIdiomStyle:];
-[_UIButtonConfigurationStyleBehaviors effectiveBehaviorWithoutButtonShapes];
-[_UIButtonConfigurationStyleBehaviors calculateMonochromaticTreatment];
-[_UIButtonConfigurationStyleBehaviors setCalculateMonochromaticTreatment:];
-[_UIButtonConfigurationStyleBehaviors effectiveMaterialFromBaseColor:state:adaptive:traitCollection:];
-[_UIButtonConfigurationStyleBehaviors styleDescription];
-[_UIButtonConfigurationStyleBehaviors effectiveActivityIndicatorColorFromEffectiveColor:state:];
-[_UIButtonConfigurationStyleBehaviors effectiveForegroundColorFromBaseColor:baseBackgroundColor:state:traitCollection:];
-[_UIButtonConfigurationStyleBehaviors setStyleDescription:];
-[_UIButtonConfigurationStyleBehaviors effectiveMonochromaticTreatmentFromBaseColor:traitCollection:];
-[_UIButtonConfigurationStyleBehaviors calculateForegroundColor];
-[_UIButtonConfigurationStyleBehaviors calculateBackgroundColor];
-[_UIButtonConfigurationStyleBehaviors effectiveBackgroundVisualEffectFromBaseColor:state:traitCollection:];
-[_UIButtonConfigurationStyleBehaviors setCalculateBackgroundColor:];
-[_UIButtonConfigurationStyleBehaviors automaticMacIdiomStyle];
-[_UIButtonConfigurationStyleBehaviors effectiveBackgroundColorFromBaseColor:state:traitCollection:];
-[_UIButtonConfigurationStyleBehaviors calculateBackgroundVisualEffect];
```
