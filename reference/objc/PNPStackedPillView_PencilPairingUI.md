# `PNPStackedPillView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PNPDeviceStateConfigurable`
- 7 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"PNPDeviceState" _deviceState;
@"UIView" _contentAreaView;
@"UILabel" _topLabel;
@"UILabel" _bottomLabel;
@"NSString" _topLabelString;
@"NSString" _bottomLabelString;
@"UIColor" _bottomLabelColor;
```

## Properties

```
@property (T@"UIColor",&,N,V_bottomLabelColor) bottomLabelColor;
@property (T@"PNPDeviceState",C,N) deviceState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PNPStackedPillView intrinsicContentSize];
-[PNPStackedPillView deviceState];
-[PNPStackedPillView layoutSubviews];
-[PNPStackedPillView setDeviceState:];
-[PNPStackedPillView _configureConstraints];
-[PNPStackedPillView bottomLabelColor];
-[PNPStackedPillView initWithFrame:topString:bottomString:];
-[PNPStackedPillView setBottomLabelColor:];
```
