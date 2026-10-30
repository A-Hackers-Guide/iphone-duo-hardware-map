# `UISSlotStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 20 properties, 33 instance methods, 2 class methods

## Instance variables

```
@"NSString" _localization;
^{CGColor=} _tintColor;
(?="all"I""{?="accessibilityButtonShapes"b1"accessibilityContrast"b1"displayRange"b2"displayScale"b3"layoutDirection"b1"legibilityWeight"b1"preferredContentSizeCategory"b4"userInterfaceIdiom"b3"userInterfaceStyle"b1"textStylePlatform"b3}) _fields;
```

## Properties

```
@property (T@"NSArray",R,N) assetAppearanceNames;
@property (Tq,R,N) assetDeviceIdiom;
@property (Tq,R,N) assetLayoutDirection;
@property (Td,R,N) assetScaleFactor;
@property (T^{__CFString=},R,N) fontContentSizeCategory;
@property (Tq,R,N) fontLegibilityWeight;
@property (Td,R,N) graphicsDisabledAlpha;
@property (TB,R,N) hasAccessibilityContentSizeCategory;
@property (TQ,R,N) accessibilityButtonShapes;
@property (TQ,R,N) accessibilityContrast;
@property (TQ,R,N) displayRange;
@property (TC,R,N) displayScale;
@property (TQ,R,N) layoutDirection;
@property (TQ,R,N) legibilityWeight;
@property (T@"NSString",R,N,V_localization) localization;
@property (TQ,R,N) preferredContentSizeCategory;
@property (T^{CGColor=},R,N,V_tintColor) tintColor;
@property (TQ,R,N) userInterfaceIdiom;
@property (TQ,R,N) userInterfaceStyle;
@property (TQ,R,N) textStylePlatform;
```

## Class methods

```
+[UISSlotStyle supportsSecureCoding];
+[UISSlotStyle slotStyleWithAccessibilityButtonShapes:accessibilityContrast:displayRange:displayScale:layoutDirection:legibilityWeight:localization:preferredContentSizeCategory:tintColor:userInterfaceIdiom:userInterfaceStyle:];
```

## Instance methods

```
-[UISSlotStyle textStylePlatform];
-[UISSlotStyle fontLegibilityWeight];
-[UISSlotStyle assetGlyphWithName:glyphSize:glyphWeight:glyphPointSize:];
-[UISSlotStyle accessibilityContrast];
-[UISSlotStyle hasAccessibilityContentSizeCategory];
-[UISSlotStyle preferredContentSizeCategory];
-[UISSlotStyle assetScaleFactor];
-[UISSlotStyle initWithAccessibilityButtonShapes:accessibilityContrast:displayRange:displayScale:layoutDirection:legibilityWeight:localization:preferredContentSizeCategory:tintColor:userInterfaceIdiom:userInterfaceStyle:textStylePlatform:];
-[UISSlotStyle fontContentSizeCategory];
-[UISSlotStyle graphicsDisabledAlpha];
-[UISSlotStyle displayScale];
-[UISSlotStyle copyWithChangeBlock:];
-[UISSlotStyle dealloc];
-[UISSlotStyle assetLayoutDirection];
-[UISSlotStyle userInterfaceIdiom];
-[UISSlotStyle layoutDirection];
-[UISSlotStyle assetDeviceIdiom];
-[UISSlotStyle initWithStyle:];
-[UISSlotStyle newFontForTextStyle:attributes:];
-[UISSlotStyle legibilityWeight];
-[UISSlotStyle gradeWithOnlyFails:allowedLocalizations:];
-[UISSlotStyle displayRange];
-[UISSlotStyle userInterfaceStyle];
-[UISSlotStyle localization];
-[UISSlotStyle assetAppearanceNames];
-[UISSlotStyle assetGlyphWithName:glyphSize:textStyle:];
-[UISSlotStyle accessibilityButtonShapes];
-[UISSlotStyle encodeWithCoder:];
-[UISSlotStyle hash];
-[UISSlotStyle tintColor];
-[UISSlotStyle initWithCoder:];
-[UISSlotStyle copyWithZone:];
-[UISSlotStyle isEqual:];
```
