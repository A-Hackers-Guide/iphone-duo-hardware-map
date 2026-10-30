# `UICellAccessory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 9 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _hidden;
@"UIColor" _backgroundColor;
q _displayedState;
d _reservedLayoutWidth;
@"UIColor" _tintColor;
q __monochromaticTreatment;
```

## Properties

```
@property (TB,R,N,G_isSystemType) isSystemType;
@property (Tq,R,N,G_systemType) systemType;
@property (T@"NSString",R,N,G_identifier) identifier;
@property (T@"UIColor",&,N,S_setBackgroundColor:,V_backgroundColor) _backgroundColor;
@property (Tq,N,S_setMonochromaticTreatment:,V__monochromaticTreatment) _monochromaticTreatment;
@property (Tq,N,V_displayedState) displayedState;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (Td,N,V_reservedLayoutWidth) reservedLayoutWidth;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
```

## Class methods

```
+[UICellAccessory supportsSecureCoding];
```

## Instance methods

```
-[UICellAccessory _systemType];
-[UICellAccessory _backgroundColor];
-[UICellAccessory setHidden:];
-[UICellAccessory init];
-[UICellAccessory displayedState];
-[UICellAccessory _systemTypePlacementForHeader:];
-[UICellAccessory isHidden];
-[UICellAccessory setTintColor:];
-[UICellAccessory _canDirectlyUpdateExistingAccessoryViewFrom:];
-[UICellAccessory setDisplayedState:];
-[UICellAccessory encodeWithCoder:];
-[UICellAccessory _setMonochromaticTreatment:];
-[UICellAccessory _compare:];
-[UICellAccessory hash];
-[UICellAccessory tintColor];
-[UICellAccessory initWithCoder:];
-[UICellAccessory copyWithZone:];
-[UICellAccessory isEqual:];
-[UICellAccessory _identifier];
-[UICellAccessory _monochromaticTreatment];
-[UICellAccessory _defaultPlacementForHeader:];
-[UICellAccessory _isDisplayedForEditingState:];
-[UICellAccessory _isSystemType];
-[UICellAccessory _setBackgroundColor:];
-[UICellAccessory reservedLayoutWidth];
-[UICellAccessory setReservedLayoutWidth:];
```
