# `_TtC15WiFiSettingsKit21NetworksListViewModel`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 35 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
WiFiSettingsKit.ScanStatus __scanStatus;
Swift.Bool _isTornDown;
_$sSh -> WiFiSettingsKit.ScannedNetwork _allNetworks;
WiFiSettingsKit.UserSettings __latestUserSettings;
Swift.Bool __receivedLiveUserSettings;
_$sScTyyt Swift.Error ? retryScanTask;
_$sSd _retryDelaySeconds;
_$sScTyyt Swift.Never ? listenScanTask;
Foundation.Date _lastNetworkRefreshTime;
Foundation.Date _lastPartialScanTime;
_$sSd networkRefreshInterval;
WiFiSettingsKit.OnceCheckedContinuation _$syyt Swift.Error ? scanFinishContinuation;
_$sScTyyt Swift.Never ? scanMonitoringTask;
_$sScTyyt Swift.Never ? scanWatchdogTask;
DispatchQueue networkUpdateQueue;
_$sSa -> WiFiSettingsKit.ScannedNetwork _knownNetworks;
_$sSa -> WiFiSettingsKit.ScannedNetwork _popularNetworks;
_$sSa -> WiFiSettingsKit.ScannedNetwork _adhocNetworks;
_$sSa -> WiFiSettingsKit.ScannedNetwork _otherNetworks;
_$sSa -> WiFiSettingsKit.ScannedNetwork _unconfiguredAccessoryNetworks;
WiFiSettingsKit.CurrentNetworkModel ? _currentNetworkModel;
WiFiSettingsKit.HotspotDevicesListModel ? _phDevicesListModel;
WiFiSettingsKit.UserSettings _userSettings;
WiFiSettingsKit.WiFiInterface ? _interface;
WiFiSettingsKit.ScanningInterface ? _scanningInterface;
WiFiSettingsKit.ScannedNetwork ? _selectedNetwork;
WiFiSettingsKit.ScannedNetwork ? _selectedHotspot;
Swift.Bool _shouldTriggerAssociation;
Dispatch.DispatchWorkItem ? _currentAssociationWorkItem;
DispatchQueue associationQueue;
Combine.AnyCancellable ? _knownNetworksChangeSubscription;
_$sSi republishEventCountForTesting;
WiFiSettingsKit.NetworksListViewModel.PendingNetworkLists ? pendingNetworkLists;
Swift.Bool networkListsFlushScheduled;
Observation.ObservationRegistrar _$observationRegistrar;
```
