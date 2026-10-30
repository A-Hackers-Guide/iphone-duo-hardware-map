# `_UIStatusBarDataCellularEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarDataNetworkEntry`
- 9 instance variables, 9 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _wifiCallingEnabled;
B _callForwardingEnabled;
B _showsSOSWhenDisabled;
B _sosAvailable;
B _isBootstrapCellular;
q _type;
@"NSString" _string;
@"NSString" _crossfadeString;
@"NSString" _badgeString;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_string) string;
@property (T@"NSString",C,N,V_crossfadeString) crossfadeString;
@property (T@"NSString",C,N,V_badgeString) badgeString;
@property (TB,N,V_wifiCallingEnabled) wifiCallingEnabled;
@property (TB,N,V_callForwardingEnabled) callForwardingEnabled;
@property (TB,N,V_showsSOSWhenDisabled) showsSOSWhenDisabled;
@property (TB,N,V_sosAvailable) sosAvailable;
@property (TB,N,V_isBootstrapCellular) isBootstrapCellular;
```

## Class methods

```
+[_UIStatusBarDataCellularEntry supportsSecureCoding];
```

## Instance methods

```
-[_UIStatusBarDataCellularEntry wifiCallingEnabled];
-[_UIStatusBarDataCellularEntry string];
-[_UIStatusBarDataCellularEntry _ui_descriptionBuilder];
-[_UIStatusBarDataCellularEntry setString:];
-[_UIStatusBarDataCellularEntry setCallForwardingEnabled:];
-[_UIStatusBarDataCellularEntry setType:];
-[_UIStatusBarDataCellularEntry type];
-[_UIStatusBarDataCellularEntry encodeWithCoder:];
-[_UIStatusBarDataCellularEntry hash];
-[_UIStatusBarDataCellularEntry initWithCoder:];
-[_UIStatusBarDataCellularEntry copyWithZone:];
-[_UIStatusBarDataCellularEntry isEqual:];
-[_UIStatusBarDataCellularEntry callForwardingEnabled];
-[_UIStatusBarDataCellularEntry crossfadeString];
-[_UIStatusBarDataCellularEntry isBootstrapCellular];
-[_UIStatusBarDataCellularEntry showsSOSWhenDisabled];
-[_UIStatusBarDataCellularEntry badgeString];
-[_UIStatusBarDataCellularEntry sosAvailable];
-[_UIStatusBarDataCellularEntry setBadgeString:];
-[_UIStatusBarDataCellularEntry setCrossfadeString:];
-[_UIStatusBarDataCellularEntry setIsBootstrapCellular:];
-[_UIStatusBarDataCellularEntry setShowsSOSWhenDisabled:];
-[_UIStatusBarDataCellularEntry setSosAvailable:];
-[_UIStatusBarDataCellularEntry setWifiCallingEnabled:];
```
