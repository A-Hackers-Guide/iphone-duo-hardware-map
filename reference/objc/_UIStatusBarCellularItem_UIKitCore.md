# `_UIStatusBarCellularItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- 9 instance variables, 10 properties, 37 instance methods, 7 class methods

## Instance variables

```
B _showsDisabledSignalBars;
B _marqueeServiceName;
@"<_UIStatusBarCellularItemTypeStringProvider>" _typeStringProvider;
@"_UIStatusBarStringView" _serviceNameView;
@"_UIStatusBarCellularSignalView" _signalView;
@"_UIStatusBarStringView" _networkTypeView;
@"_UIStatusBarImageView" _warningView;
@"_UIStatusBarImageView" _callForwardingView;
@"_UIStatusBarStringView" _rawStringView;
```

## Properties

```
@property (T@"NSString",R,N) cellularDataEntryKey;
@property (T@"_UIStatusBarStringView",&,N,V_serviceNameView) serviceNameView;
@property (T@"_UIStatusBarCellularSignalView",&,N,V_signalView) signalView;
@property (T@"_UIStatusBarStringView",&,N,V_networkTypeView) networkTypeView;
@property (T@"_UIStatusBarImageView",&,N,V_warningView) warningView;
@property (T@"_UIStatusBarImageView",&,N,V_callForwardingView) callForwardingView;
@property (T@"_UIStatusBarStringView",&,N,V_rawStringView) rawStringView;
@property (TB,N,V_showsDisabledSignalBars) showsDisabledSignalBars;
@property (TB,N,V_marqueeServiceName) marqueeServiceName;
@property (T@"<_UIStatusBarCellularItemTypeStringProvider>",W,N,V_typeStringProvider) typeStringProvider;
```

## Class methods

```
+[_UIStatusBarCellularItem groupWithHighPriority:lowPriority:typeClass:allowDualNetwork:];
+[_UIStatusBarCellularItem callForwardingDisplayIdentifier];
+[_UIStatusBarCellularItem signalStrengthDisplayIdentifier];
+[_UIStatusBarCellularItem nameDisplayIdentifier];
+[_UIStatusBarCellularItem rawDisplayIdentifier];
+[_UIStatusBarCellularItem typeDisplayIdentifier];
+[_UIStatusBarCellularItem warningDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarCellularItem initWithIdentifier:statusBar:];
-[_UIStatusBarCellularItem _create_rawStringView];
-[_UIStatusBarCellularItem viewForIdentifier:];
-[_UIStatusBarCellularItem _stringForCellularType:];
-[_UIStatusBarCellularItem setRawStringView:];
-[_UIStatusBarCellularItem signalView];
-[_UIStatusBarCellularItem rawStringView];
-[_UIStatusBarCellularItem setSignalView:];
-[_UIStatusBarCellularItem entryForDisplayItemWithIdentifier:];
-[_UIStatusBarCellularItem _create_signalView];
-[_UIStatusBarCellularItem dependentEntryKeys];
-[_UIStatusBarCellularItem _backgroundColorForUpdate:entry:];
-[_UIStatusBarCellularItem applyUpdate:toDisplayItem:];
-[_UIStatusBarCellularItem prepareAnimation:forDisplayItem:];
-[_UIStatusBarCellularItem _fillColorForUpdate:entry:];
-[_UIStatusBarCellularItem cellularDataEntryKey];
-[_UIStatusBarCellularItem _showCallFowardingForEntry:];
-[_UIStatusBarCellularItem serviceNameView];
-[_UIStatusBarCellularItem networkTypeView];
-[_UIStatusBarCellularItem setWarningView:];
-[_UIStatusBarCellularItem _create_callForwardingView];
-[_UIStatusBarCellularItem _create_networkTypeView];
-[_UIStatusBarCellularItem _create_serviceNameView];
-[_UIStatusBarCellularItem _create_warningView];
-[_UIStatusBarCellularItem _updateSignalView:withUpdate:entry:forceShowingDisabledSignalBars:];
-[_UIStatusBarCellularItem callForwardingView];
-[_UIStatusBarCellularItem marqueeServiceName];
-[_UIStatusBarCellularItem setCallForwardingView:];
-[_UIStatusBarCellularItem setMarqueeServiceName:];
-[_UIStatusBarCellularItem setNetworkTypeView:];
-[_UIStatusBarCellularItem setServiceNameView:];
-[_UIStatusBarCellularItem setShowsDisabledSignalBars:];
-[_UIStatusBarCellularItem setTypeStringProvider:];
-[_UIStatusBarCellularItem setmarqueeServiceName:];
-[_UIStatusBarCellularItem showsDisabledSignalBars];
-[_UIStatusBarCellularItem typeStringProvider];
-[_UIStatusBarCellularItem warningView];
```
