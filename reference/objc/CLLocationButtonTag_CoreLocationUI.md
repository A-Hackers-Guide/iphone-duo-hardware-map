# `CLLocationButtonTag`

- Image: [`/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI`](../userland/System__Library__Frameworks__CoreLocationUI.framework__CoreLocationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISSlotTag`
- Protocols: `NSSecureCoding`
- 10 instance variables, 12 properties, 34 instance methods, 3 class methods

## Instance variables

```
B _renderedSuccessfully;
i _controlSize;
d _fontSize;
q _label;
q _icon;
@"UIColor" _backgroundColor;
@"UIColor" _tintColor;
d _cornerRadius;
@"UISSlotStyle" _style;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (Td,N,V_fontSize) fontSize;
@property (Tq,N,V_label) label;
@property (Tq,N,V_icon) icon;
@property (T@"UIColor",&,N,V_backgroundColor) backgroundColor;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T@"UISSlotStyle",&,N,V_style) style;
@property (TB,N,V_renderedSuccessfully) renderedSuccessfully;
@property (Ti,N,V_controlSize) controlSize;
@property (Td,R,D,N) buttonWidth;
@property (Td,R,D,N) buttonHeight;
```

## Class methods

```
+[CLLocationButtonTag supportsSecureCoding];
+[CLLocationButtonTag cacheLimit];
+[CLLocationButtonTag secureNameForLabel:];
```

## Instance methods

```
-[CLLocationButtonTag setFontSize:];
-[CLLocationButtonTag resolvedStyleForStyle:];
-[CLLocationButtonTag fontSize];
-[CLLocationButtonTag label];
-[CLLocationButtonTag setLabel:];
-[CLLocationButtonTag setIcon:];
-[CLLocationButtonTag secureNameForStyle:];
-[CLLocationButtonTag style];
-[CLLocationButtonTag setCornerRadius:];
-[CLLocationButtonTag setStyle:];
-[CLLocationButtonTag setBackgroundColor:];
-[CLLocationButtonTag authenticationMessageContextForStyle:];
-[CLLocationButtonTag setTintColor:];
-[CLLocationButtonTag cornerRadius];
-[CLLocationButtonTag encodeWithCoder:];
-[CLLocationButtonTag isValid];
-[CLLocationButtonTag buttonHeight];
-[CLLocationButtonTag setFrame:];
-[CLLocationButtonTag backgroundColor];
-[CLLocationButtonTag tintColor];
-[CLLocationButtonTag setControlSize:];
-[CLLocationButtonTag initWithCoder:];
-[CLLocationButtonTag copyWithZone:];
-[CLLocationButtonTag isEqual:];
-[CLLocationButtonTag frame];
-[CLLocationButtonTag icon];
-[CLLocationButtonTag buttonWidth];
-[CLLocationButtonTag controlSize];
-[CLLocationButtonTag hitTestInformationMaskForStyle:];
-[CLLocationButtonTag failGradeForStyle:];
-[CLLocationButtonTag contrastValidForBgColorAndFgTextWithCumulativeOpacity:];
-[CLLocationButtonTag initWithLabel:iconType:backgroundColor:tintColor:cornerRadius:frame:fontSize:controlSize:];
-[CLLocationButtonTag renderedSuccessfully];
-[CLLocationButtonTag setRenderedSuccessfully:];
```
