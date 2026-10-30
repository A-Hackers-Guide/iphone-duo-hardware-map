# `CTTelephonyNetworkInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientDataDelegateInternal`, `CoreTelephonyClientCarrierBundleDelegateInternal`
- 9 instance variables, 15 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"CoreTelephonyClient" _client;
@"<CTTelephonyNetworkInfoDelegate>" _delegate;
@? _serviceSubscriberCellularProvidersDidUpdateNotifier;
@? _subscriberCellularProviderDidUpdateNotifier;
B _initialized;
@"CTServiceDescriptorContainer" _descriptors;
@"NSMutableDictionary" _serviceSubscriberCellularProviders;
@"NSMutableDictionary" _cachedCurrentRadioAccessTechnology;
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _clientQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_serviceSubscriberCellularProviders) serviceSubscriberCellularProviders;
@property (T@"NSMutableDictionary",&,V_cachedCurrentRadioAccessTechnology) cachedCurrentRadioAccessTechnology;
@property (T@"CTServiceDescriptorContainer",R,V_descriptors) descriptors;
@property (T{queue={object=^{dispatch_object_s}}},V_clientQueue) clientQueue;
@property (T@"NSString",R,C) dataServiceIdentifier;
@property (T@"<CTTelephonyNetworkInfoDelegate>",W) delegate;
@property (T@"CTCarrier",R,&) subscriberCellularProvider;
@property (T@?,C,N,V_serviceSubscriberCellularProvidersDidUpdateNotifier) serviceSubscriberCellularProvidersDidUpdateNotifier;
@property (T@?,C,N) subscriberCellularProviderDidUpdateNotifier;
@property (T@"NSDictionary",R,&,N) serviceCurrentRadioAccessTechnology;
@property (T@"NSString",R,&,N) currentRadioAccessTechnology;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CTTelephonyNetworkInfo setClientQueue:];
-[CTTelephonyNetworkInfo signalStrength];
-[CTTelephonyNetworkInfo clientQueue];
-[CTTelephonyNetworkInfo carrierBundleChange:];
-[CTTelephonyNetworkInfo setSubscriberCellularProviderDidUpdateNotifier:];
-[CTTelephonyNetworkInfo setCachedCurrentRadioAccessTechnology:];
-[CTTelephonyNetworkInfo serviceSubscriberCellularProviders];
-[CTTelephonyNetworkInfo setServiceSubscriberCellularProviders:];
-[CTTelephonyNetworkInfo initWithClient:];
-[CTTelephonyNetworkInfo dataServiceIdentifier];
-[CTTelephonyNetworkInfo init];
-[CTTelephonyNetworkInfo getCarrierName:forContext:withError:];
-[CTTelephonyNetworkInfo cachedCurrentRadioAccessTechnology];
-[CTTelephonyNetworkInfo dealloc];
-[CTTelephonyNetworkInfo queryRat];
-[CTTelephonyNetworkInfo serviceSubscribersCellularProviderDidUpdateNotifier];
-[CTTelephonyNetworkInfo descriptors];
-[CTTelephonyNetworkInfo cellId];
-[CTTelephonyNetworkInfo getMobileCountryCode:andIsoCountryCode:forContext:withError:];
-[CTTelephonyNetworkInfo getMobileNetworkCode:forContext:withError:];
-[CTTelephonyNetworkInfo setDelegate:];
-[CTTelephonyNetworkInfo updateRat:descriptor:];
-[CTTelephonyNetworkInfo currentRadioAccessTechnology];
-[CTTelephonyNetworkInfo updateLegacyRat:];
-[CTTelephonyNetworkInfo getAllowsVOIP:forContext:withError:];
-[CTTelephonyNetworkInfo updateNetworkInfoAndShouldNotifyClient:forContext:];
-[CTTelephonyNetworkInfo queryRatForDescriptor:];
-[CTTelephonyNetworkInfo delegate];
-[CTTelephonyNetworkInfo radioAccessTechnology];
-[CTTelephonyNetworkInfo serviceSignalStrength];
-[CTTelephonyNetworkInfo subscriberCellularProviderDidUpdateNotifier];
-[CTTelephonyNetworkInfo regDataModeChanged:dataMode:];
-[CTTelephonyNetworkInfo serviceCellId];
-[CTTelephonyNetworkInfo subscriberCellularProvider];
-[CTTelephonyNetworkInfo currentDataServiceDescriptorChanged:];
-[CTTelephonyNetworkInfo serviceCurrentRadioAccessTechnology];
-[CTTelephonyNetworkInfo postNotificationIfReady:object:];
-[CTTelephonyNetworkInfo setServiceSubscriberCellularProvidersDidUpdateNotifier:];
-[CTTelephonyNetworkInfo serviceSubscriberCellularProvidersDidUpdateNotifier];
-[CTTelephonyNetworkInfo setServiceSubscriberCellularProviderDidUpdateNotifier:];
```
