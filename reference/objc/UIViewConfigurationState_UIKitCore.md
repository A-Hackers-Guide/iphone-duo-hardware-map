# `UIViewConfigurationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewConfigurationStateReadonly`, `UIConfigurationState`
- 4 instance variables, 13 properties, 32 instance methods, 1 class methods

## Instance variables

```
Q _mutations;
@"NSMutableDictionary" _customStates;
{?="isDisabled"b1"isHighlighted"b1"isSelected"b1"isFocused"b1"isPinned"b1} _stateFlags;
@"UITraitCollection" _traitCollection;
```

## Properties

```
@property (TQ,R,N) _mutations;
@property (Tq,N,S_setContextMenuGroupLocation:) _contextMenuGroupLocation;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (TB,N,GisDisabled) disabled;
@property (TB,N,GisHighlighted) highlighted;
@property (TB,N,GisSelected) selected;
@property (TB,N,GisFocused) focused;
@property (TB,N,GisPinned) pinned;
@property (TQ,R,N) _viewConfigurationState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIViewConfigurationState supportsSecureCoding];
```

## Instance methods

```
-[UIViewConfigurationState _setSwiftBridgingCustomState:forKey:];
-[UIViewConfigurationState setTraitCollection:];
-[UIViewConfigurationState setPinned:];
-[UIViewConfigurationState setSelected:];
-[UIViewConfigurationState isPinned];
-[UIViewConfigurationState _initWithState:];
-[UIViewConfigurationState setFocused:];
-[UIViewConfigurationState traitCollection];
-[UIViewConfigurationState isHighlighted];
-[UIViewConfigurationState _contextMenuGroupLocation];
-[UIViewConfigurationState _setContextMenuGroupLocation:];
-[UIViewConfigurationState objectForKeyedSubscript:];
-[UIViewConfigurationState isFocused];
-[UIViewConfigurationState isDisabled];
-[UIViewConfigurationState _configureWithViewConfigurationState:];
-[UIViewConfigurationState setHighlighted:];
-[UIViewConfigurationState encodeWithCoder:];
-[UIViewConfigurationState isSelected];
-[UIViewConfigurationState customStateForKey:];
-[UIViewConfigurationState setCustomState:forKey:];
-[UIViewConfigurationState hash];
-[UIViewConfigurationState description];
-[UIViewConfigurationState _mutations];
-[UIViewConfigurationState initWithCoder:];
-[UIViewConfigurationState initWithTraitCollection:];
-[UIViewConfigurationState copyWithZone:];
-[UIViewConfigurationState _appendPropertiesForDescription:];
-[UIViewConfigurationState isEqual:];
-[UIViewConfigurationState setObject:forKeyedSubscript:];
-[UIViewConfigurationState _customStatesForSwiftBridging];
-[UIViewConfigurationState setDisabled:];
-[UIViewConfigurationState _viewConfigurationState];
```
