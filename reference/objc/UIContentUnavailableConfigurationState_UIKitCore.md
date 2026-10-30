# `UIContentUnavailableConfigurationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentUnavailableConfigurationStateReadonly`, `UIConfigurationState`
- 5 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
Q _mutations;
@"NSMutableDictionary" _customStates;
{?=} _stateFlags;
@"UITraitCollection" _traitCollection;
@"NSString" _searchText;
```

## Properties

```
@property (TQ,R,N) _mutations;
@property (T@"NSString",&,N) searchControllerText;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (T@"NSString",&,N,V_searchText) searchText;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIContentUnavailableConfigurationState supportsSecureCoding];
```

## Instance methods

```
-[UIContentUnavailableConfigurationState _setSwiftBridgingCustomState:forKey:];
-[UIContentUnavailableConfigurationState setTraitCollection:];
-[UIContentUnavailableConfigurationState traitCollection];
-[UIContentUnavailableConfigurationState searchText];
-[UIContentUnavailableConfigurationState objectForKeyedSubscript:];
-[UIContentUnavailableConfigurationState searchControllerText];
-[UIContentUnavailableConfigurationState setSearchText:];
-[UIContentUnavailableConfigurationState encodeWithCoder:];
-[UIContentUnavailableConfigurationState customStateForKey:];
-[UIContentUnavailableConfigurationState setCustomState:forKey:];
-[UIContentUnavailableConfigurationState hash];
-[UIContentUnavailableConfigurationState description];
-[UIContentUnavailableConfigurationState _mutations];
-[UIContentUnavailableConfigurationState initWithCoder:];
-[UIContentUnavailableConfigurationState initWithTraitCollection:];
-[UIContentUnavailableConfigurationState copyWithZone:];
-[UIContentUnavailableConfigurationState isEqual:];
-[UIContentUnavailableConfigurationState setObject:forKeyedSubscript:];
-[UIContentUnavailableConfigurationState _customStatesForSwiftBridging];
-[UIContentUnavailableConfigurationState setSearchControllerText:];
```
