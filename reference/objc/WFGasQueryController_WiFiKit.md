# `WFGasQueryController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<WFGasQueryControllerDelegate>" _delegate;
@"NSSet" _profiles;
@"NSMapTable" _gasResponseCache;
@"NSMutableSet" _resolvedNetworks;
@"WFInterface" _interface;
@"CWFInterface" _cInterface;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_gasResponseCache) gasResponseCache;
@property (T@"NSMutableSet",&,N,V_resolvedNetworks) resolvedNetworks;
@property (T@"WFInterface",&,N,V_interface) interface;
@property (T@"CWFInterface",&,N,V_cInterface) cInterface;
@property (T@"<WFGasQueryControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,N,V_profiles) profiles;
```

## Instance methods

```
-[WFGasQueryController init];
-[WFGasQueryController initWithInterface:];
-[WFGasQueryController setInterface:];
-[WFGasQueryController setCInterface:];
-[WFGasQueryController setDelegate:];
-[WFGasQueryController interface];
-[WFGasQueryController profiles];
-[WFGasQueryController cInterface];
-[WFGasQueryController delegate];
-[WFGasQueryController _ANQPDictionaryFromScanResult:];
-[WFGasQueryController _defaultANQPParameterForNetworks:];
-[WFGasQueryController _processANQPResults:scanRecords:error:];
-[WFGasQueryController gasResponseCache];
-[WFGasQueryController profileForNetwork:];
-[WFGasQueryController removeAllProfiles];
-[WFGasQueryController removeProfileForNetwork:];
-[WFGasQueryController resolveProfileForNetwork:handler:force:];
-[WFGasQueryController resolveProfilesForNetworks:];
-[WFGasQueryController resolvedNetworks];
-[WFGasQueryController setGasResponseCache:];
-[WFGasQueryController setResolvedNetworks:];
```
