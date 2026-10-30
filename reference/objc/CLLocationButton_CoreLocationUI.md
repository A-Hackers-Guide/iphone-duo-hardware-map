# `CLLocationButton`

- Image: [`/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI`](../userland/System__Library__Frameworks__CoreLocationUI.framework__CoreLocationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `NSSecureCoding`
- 17 instance variables, 8 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"_UISlotView" _slotView;
@"UIColor" _backgroundColor;
@"UIColor" _tintColor;
@"UIColor" _resolvedBackgroundColor;
@"UIColor" _resolvedTintColor;
@"NSString" _sandboxExtension;
{CGSize="width"d"height"d} _intrinsicSize;
@"NSLayoutConstraint" _minimumWidthConstraint;
@"NSLayoutConstraint" _minimumHeightConstraint;
@"<LocationUIProtocol>" _proxy;
B _colorsIllegible;
B _alphaInsufficient;
i _controlSize;
q _icon;
q _label;
d _fontSize;
d _cornerRadius;
```

## Properties

```
@property (T@"<LocationUIProtocol>",R,N) locationUIProxy;
@property (TB,R,N,V_colorsIllegible) colorsIllegible;
@property (TB,R,N,V_alphaInsufficient) alphaInsufficient;
@property (Ti,N,V_controlSize) controlSize;
@property (Tq,N,V_icon) icon;
@property (Tq,N,V_label) label;
@property (Td,N,V_fontSize) fontSize;
@property (Td,N,V_cornerRadius) cornerRadius;
```

## Class methods

```
+[CLLocationButton supportsSecureCoding];
```

## Instance methods

```
-[CLLocationButton _controlEventsForActionTriggered];
-[CLLocationButton intrinsicContentSize];
-[CLLocationButton setFontSize:];
-[CLLocationButton fontSize];
-[CLLocationButton init];
-[CLLocationButton label];
-[CLLocationButton setLabel:];
-[CLLocationButton setIcon:];
-[CLLocationButton layoutSubviews];
-[CLLocationButton setCornerRadius:];
-[CLLocationButton markDirty];
-[CLLocationButton setBackgroundColor:];
-[CLLocationButton sizeThatFits:];
-[CLLocationButton setTintColor:];
-[CLLocationButton cornerRadius];
-[CLLocationButton encodeWithCoder:];
-[CLLocationButton backgroundColor];
-[CLLocationButton tintColor];
-[CLLocationButton setControlSize:];
-[CLLocationButton initWithCoder:];
-[CLLocationButton _populateArchivedSubviews:];
-[CLLocationButton initWithFrame:];
-[CLLocationButton icon];
-[CLLocationButton _secureName];
-[CLLocationButton _sendActionsForEvents:withEvent:];
-[CLLocationButton _setupSlotView];
-[CLLocationButton controlSize];
-[CLLocationButton colorsIllegible];
-[CLLocationButton locationUIProxy];
-[CLLocationButton _actionForPreSetTarget];
-[CLLocationButton _computeLocationButtonTag];
-[CLLocationButton _yieldSlotViewContentForLayerContextID:slotStyle:withYieldBlock:];
-[CLLocationButton alphaInsufficient];
-[CLLocationButton convertToControlSize:];
```
