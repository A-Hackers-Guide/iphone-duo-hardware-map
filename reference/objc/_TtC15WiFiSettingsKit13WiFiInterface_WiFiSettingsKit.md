# `_TtC15WiFiSettingsKit13WiFiInterface`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtC15WiFiSettingsKit22StateObserverInterface`
- 23 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
_$sSo12CWFInterfaceC cwfInterface;
WiFiSettingsKit.WiFiInterfaceState state;
Swift.Int32 cellularOutrankNotificationToken;
_$sySa -> WiFiSettingsKit.ScannedNetwork _$sGcSg onScanResultsChanged;
_$syycSg onScanDidFinish;
WiFiSettingsKit.UserSettings _$scSg -> onUserSettingsChanged;
Combine.Published Swift.Bool _scanDidFinish;
_$sSo23WSKHotspotHelperScannerCSg hotspotHelperScanner;
WiFiSettingsKit.HotspotHelperScannerDelegate ? hotspotHelperDelegate;
_$sSa -> WiFiSettingsKit.HotspotHelperNetwork _hotspotHelperNetworks;
_$sSa -> __C.CWFEventType monitoredEvents;
_$sScTyyt Swift.Never ? scanTask;
_$sScTyyt Swift.Never ? associationTask;
WiFiSettingsKit.NetworkRepresentation ? currentNetwork;
os.OSAllocatedUnfairLock _$sSaySo17CWFNetworkProfileCG _profilesLock;
WiFiSettingsKit.WiFiLQM ? currentLQM;
__C.CWFWiFiUIStateFlags cachedWiFiUIStateFlags;
Combine.Published _$sySa -> WiFiSettingsKit.NetworkWarning _currentNetworkWarnings;
_$sSSSg hardwareMACAddress;
Combine.Published _$sSSSg _currentNetworkSubtitle;
_$sSo17CWFNetworkProfileCSg cachedCurrentNetworkProfile;
os.OSAllocatedUnfairLock _$sySDyS2S_ WiFiSettingsKit.PrivateMACAddressMode _$stG privateMACCache;
Swift.Bool currentNetworkRefreshScheduled;
```
