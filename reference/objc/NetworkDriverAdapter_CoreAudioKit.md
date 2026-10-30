# `NetworkDriverAdapter`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 8 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSString" mComputerName;
@"NetServiceDirectory" mBonjourDirectory;
@"NetAddressBook2" mAddressBook;
I mMIDIClient;
I mMIDIPort;
I mMIDI2Port;
I mMIDIDevice;
I mSelectedMIDISource;
@"NSMutableArray" mSessions;
I mMIDIUMPDevice;
@"NSMutableArray" mCachedSources;
@"NSMutableArray" mCachedDestinations;
^{__SCPreferences=} mSysPrefs;
{unique_ptr<NetworkDriverRTData, std::default_delete<NetworkDriverRTData>>=""{?="__ptr_"^{NetworkDriverRTData}}} mRealtimeData;
@? onSessionsChanged;
@? onDirectoryChanged;
@? onSessionDetailsChanged;
@? onConnectionStatusChanged;
@? onErrorOccurred;
```

## Properties

```
@property (T@?,C,N,VonSessionsChanged) onSessionsChanged;
@property (T@?,C,N,VonDirectoryChanged) onDirectoryChanged;
@property (T@?,C,N,VonSessionDetailsChanged) onSessionDetailsChanged;
@property (T@?,C,N,VonConnectionStatusChanged) onConnectionStatusChanged;
@property (T@?,C,N,VonErrorOccurred) onErrorOccurred;
@property (TB,R,N) foundNetworkDevice;
@property (TB,R,N) foundUMPNetworkDevice;
@property (TB,R,N) networkMIDI2Enabled;
```

## Instance methods

```
-[NetworkDriverAdapter cleanup];
-[NetworkDriverAdapter init];
-[NetworkDriverAdapter sessions];
-[NetworkDriverAdapter dealloc];
-[NetworkDriverAdapter addSession:];
-[NetworkDriverAdapter syncSessionState];
-[NetworkDriverAdapter entityPropertyChanged:property:];
-[NetworkDriverAdapter getLatencyData:];
-[NetworkDriverAdapter onErrorOccurred];
-[NetworkDriverAdapter addAddressBookEntry:];
-[NetworkDriverAdapter addressBookEntriesWithType:];
-[NetworkDriverAdapter bonjourServicesWithType:];
-[NetworkDriverAdapter deleteAddressBookEntry:];
-[NetworkDriverAdapter deviceErrorsChanged];
-[NetworkDriverAdapter foundNetworkDevice];
-[NetworkDriverAdapter foundUMPNetworkDevice];
-[NetworkDriverAdapter getMIDIDestinations];
-[NetworkDriverAdapter getMIDISources];
-[NetworkDriverAdapter iaContextualHelpButtonPressed];
-[NetworkDriverAdapter isRendezvousServiceLocal:selectedSession:];
-[NetworkDriverAdapter isRendezvousServiceSelectable:selectedSession:];
-[NetworkDriverAdapter networkMIDI2Enabled];
-[NetworkDriverAdapter notifyConnectionStatusChanged:serviceName:];
-[NetworkDriverAdapter notifyDirectoryChanged];
-[NetworkDriverAdapter notifyError:];
-[NetworkDriverAdapter notifySessionDetailsChanged:];
-[NetworkDriverAdapter notifySessionsChanged];
-[NetworkDriverAdapter observeLatencyForSession:];
-[NetworkDriverAdapter onConnectionStatusChanged];
-[NetworkDriverAdapter onDirectoryChanged];
-[NetworkDriverAdapter onSessionDetailsChanged];
-[NetworkDriverAdapter onSessionsChanged];
-[NetworkDriverAdapter prunePersistentPeers];
-[NetworkDriverAdapter removeSessionWithEntityID:];
-[NetworkDriverAdapter sessionLocalNameIsDuplicate:selectedSession:];
-[NetworkDriverAdapter sessionNetworkNameIsDuplicate:selectedSession:];
-[NetworkDriverAdapter setOnConnectionStatusChanged:];
-[NetworkDriverAdapter setOnDirectoryChanged:];
-[NetworkDriverAdapter setOnErrorOccurred:];
-[NetworkDriverAdapter setOnSessionDetailsChanged:];
-[NetworkDriverAdapter setOnSessionsChanged:];
-[NetworkDriverAdapter updateAddressBookEntry:];
-[NetworkDriverAdapter updateMIDIEndpointCache];
-[NetworkDriverAdapter visibleServicesDidChange:];
```
