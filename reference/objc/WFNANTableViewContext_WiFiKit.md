# `WFNANTableViewContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAwarePublisherDelegate`, `WiFiAwareSubscriberDelegate`
- 5 instance variables, 9 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _publishers;
@"NSMutableDictionary" _dataSessionsForPublish;
@"NSMutableArray" _subscribers;
@"NSMutableDictionary" _discoveryResults;
@"NSMutableDictionary" _dataSessionsForSubscribe;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_publishers) publishers;
@property (T@"NSMutableDictionary",&,N,V_dataSessionsForPublish) dataSessionsForPublish;
@property (T@"NSMutableArray",&,N,V_subscribers) subscribers;
@property (T@"NSMutableDictionary",&,N,V_discoveryResults) discoveryResults;
@property (T@"NSMutableDictionary",&,N,V_dataSessionsForSubscribe) dataSessionsForSubscribe;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFNANTableViewContext init];
-[WFNANTableViewContext publishers];
-[WFNANTableViewContext removeSubscriber:];
-[WFNANTableViewContext addSubscriber:];
-[WFNANTableViewContext publisher:terminatedWithReason:];
-[WFNANTableViewContext setSubscribers:];
-[WFNANTableViewContext publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:];
-[WFNANTableViewContext publisher:dataTerminatedForHandle:reason:];
-[WFNANTableViewContext publisher:failedToStartWithError:];
-[WFNANTableViewContext publisherStarted:];
-[WFNANTableViewContext subscriber:failedToStartWithError:];
-[WFNANTableViewContext subscriber:lostDiscoveryResultForPublishID:address:];
-[WFNANTableViewContext subscriber:receivedDiscoveyResult:];
-[WFNANTableViewContext subscriber:terminatedWithReason:];
-[WFNANTableViewContext subscriberStarted:];
-[WFNANTableViewContext subscribers];
-[WFNANTableViewContext setPublishers:];
-[WFNANTableViewContext addPublisher:];
-[WFNANTableViewContext removeDataSession:forPublisher:];
-[WFNANTableViewContext addDataSession:forPublisher:];
-[WFNANTableViewContext addDataSession:forSubscriber:];
-[WFNANTableViewContext addDiscoveryResult:forSubscriber:];
-[WFNANTableViewContext dataSessionsForPublish];
-[WFNANTableViewContext dataSessionsForSubscribe];
-[WFNANTableViewContext discoveryResults];
-[WFNANTableViewContext getDataSessionAtIndex:forPublisher:];
-[WFNANTableViewContext getDataSessionAtIndex:forSubscriber:];
-[WFNANTableViewContext getDataSessionsCountForPublisher:];
-[WFNANTableViewContext getDataSessionsCountForSubscriber:];
-[WFNANTableViewContext getDataSessionsForPublisher:];
-[WFNANTableViewContext getDataSessionsForSubscriber:];
-[WFNANTableViewContext getDiscoveryResultAtIndex:forSubscriber:];
-[WFNANTableViewContext getDiscoveryResultsCountForSubscriber:];
-[WFNANTableViewContext getDiscoveryResultsForSubscriber:];
-[WFNANTableViewContext getPublisherAtIndex:];
-[WFNANTableViewContext getPublishers];
-[WFNANTableViewContext getPublishersCount];
-[WFNANTableViewContext getSubscriberAtIndex:];
-[WFNANTableViewContext getSubscribers];
-[WFNANTableViewContext getSubscribersCount];
-[WFNANTableViewContext removeDataSession:forSubscriber:];
-[WFNANTableViewContext removeDiscoveryResultWithPublishID:andPublisherAddress:forSubscriber:];
-[WFNANTableViewContext removePublisher:];
-[WFNANTableViewContext removePublisherAtIndex:];
-[WFNANTableViewContext removeSubscriberAtIndex:];
-[WFNANTableViewContext setDataSessionsForPublish:];
-[WFNANTableViewContext setDataSessionsForSubscribe:];
-[WFNANTableViewContext setDiscoveryResults:];
```
