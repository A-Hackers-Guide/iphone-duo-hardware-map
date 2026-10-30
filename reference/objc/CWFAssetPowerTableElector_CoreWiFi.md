# `CWFAssetPowerTableElector`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 29 instance variables, 29 properties, 88 instance methods, 2 class methods

## Instance variables

```
B __isInternalBuild;
B __interfaceAddedEventOccurred;
B __driverAvailEventOccurred;
B __readyToFetchLoadedPT;
B __powerTableFetched;
i __pid;
@"<CWFAssetPowerTableElectorDelegate>" _delegate;
@"CWFInterface" _wifiInterface;
@"NSString" __powerTableSession;
q __powerTableEvaluationState;
d __maxSessionActiveInterval;
d __readinessTimeoutInterval;
d __votingTimeoutInterval;
d __dateToBlockWaitingForDriverReload;
d __dateToFetchReloadedPowerTableForVoteAssesment;
@"NSError" _error;
@"NSObject<OS_dispatch_queue>" __coordinationQueue;
@"NSObject<OS_dispatch_queue>" __apiQueue;
@"NSObject<OS_dispatch_queue>" __signalQueue;
@"NSObject<OS_dispatch_queue>" __waitingQueue;
@"NSNotificationCenter" __notificationCenter;
@"NSDistributedNotificationCenter" __distNotificationCenter;
@"NSDate" __powerTableSessionStartDate;
@"NSDate" __powerTableEvaluationStartDate;
@"NSDate" __powerTableRequestingVotesStartDate;
@"NSCondition" __interfaceAddedEventCondition;
@"NSCondition" __driverAvailEventCondition;
@"NSCondition" __readyToFetchLoadedPTCondition;
@"NSCondition" __condPowerTableFetched;
```

## Properties

```
@property (T@"CWFInterface",&,N,V_wifiInterface) wifiInterface;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__coordinationQueue) _coordinationQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__apiQueue) _apiQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__signalQueue) _signalQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__waitingQueue) _waitingQueue;
@property (T@"NSNotificationCenter",&,N,V__notificationCenter) _notificationCenter;
@property (T@"NSDistributedNotificationCenter",&,N,V__distNotificationCenter) _distNotificationCenter;
@property (T@"NSString",&,N,V__powerTableSession) _powerTableSession;
@property (T@"NSDate",&,N,V__powerTableSessionStartDate) _powerTableSessionStartDate;
@property (T@"NSDate",&,N,V__powerTableEvaluationStartDate) _powerTableEvaluationStartDate;
@property (T@"NSDate",&,N,V__powerTableRequestingVotesStartDate) _powerTableRequestingVotesStartDate;
@property (Ti,N,V__pid) _pid;
@property (TB,N,V__isInternalBuild) _isInternalBuild;
@property (Tq,N,V__powerTableEvaluationState) _powerTableEvaluationState;
@property (T@"NSCondition",&,N,V__interfaceAddedEventCondition) _interfaceAddedEventCondition;
@property (TB,N,V__interfaceAddedEventOccurred) _interfaceAddedEventOccurred;
@property (T@"NSCondition",&,N,V__driverAvailEventCondition) _driverAvailEventCondition;
@property (TB,N,V__driverAvailEventOccurred) _driverAvailEventOccurred;
@property (T@"NSCondition",&,N,V__readyToFetchLoadedPTCondition) _readyToFetchLoadedPTCondition;
@property (TB,N,V__readyToFetchLoadedPT) _readyToFetchLoadedPT;
@property (T@"NSCondition",&,N,V__condPowerTableFetched) _condPowerTableFetched;
@property (TB,N,V__powerTableFetched) _powerTableFetched;
@property (T@"NSError",&,N,V_error) error;
@property (T@"<CWFAssetPowerTableElectorDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V__maxSessionActiveInterval) _maxSessionActiveInterval;
@property (Td,N,V__readinessTimeoutInterval) _readinessTimeoutInterval;
@property (Td,N,V__votingTimeoutInterval) _votingTimeoutInterval;
@property (Td,N,V__dateToBlockWaitingForDriverReload) _dateToBlockWaitingForDriverReload;
@property (Td,N,V__dateToFetchReloadedPowerTableForVoteAssesment) _dateToFetchReloadedPowerTableForVoteAssesment;
```

## Class methods

```
+[CWFAssetPowerTableElector powerTableEvaluationStateAsString:];
+[CWFAssetPowerTableElector powerTableEvaluationStringToState:];
```

## Instance methods

```
-[CWFAssetPowerTableElector setError:];
-[CWFAssetPowerTableElector _notificationCenter];
-[CWFAssetPowerTableElector _isInternalBuild];
-[CWFAssetPowerTableElector dealloc];
-[CWFAssetPowerTableElector error];
-[CWFAssetPowerTableElector setDelegate:];
-[CWFAssetPowerTableElector delegate];
-[CWFAssetPowerTableElector description];
-[CWFAssetPowerTableElector _coordinationQueue];
-[CWFAssetPowerTableElector initWithNotificationCenter:];
-[CWFAssetPowerTableElector set_notificationCenter:];
-[CWFAssetPowerTableElector persist:forKey:];
-[CWFAssetPowerTableElector powerTableVote:];
-[CWFAssetPowerTableElector set_powerTableSessionStartDate:];
-[CWFAssetPowerTableElector _apiQueue];
-[CWFAssetPowerTableElector _condPowerTableFetched];
-[CWFAssetPowerTableElector _dateToBlockWaitingForDriverReload];
-[CWFAssetPowerTableElector _dateToFetchReloadedPowerTableForVoteAssesment];
-[CWFAssetPowerTableElector _distNotificationCenter];
-[CWFAssetPowerTableElector _driverAvailEventCondition];
-[CWFAssetPowerTableElector _driverAvailEventOccurred];
-[CWFAssetPowerTableElector _handleCENPowerTableEvaluationNotification:];
-[CWFAssetPowerTableElector _interfaceAddedEventCondition];
-[CWFAssetPowerTableElector _interfaceAddedEventOccurred];
-[CWFAssetPowerTableElector _maxSessionActiveInterval];
-[CWFAssetPowerTableElector _pid];
-[CWFAssetPowerTableElector _powerTableEvaluationStartDate];
-[CWFAssetPowerTableElector _powerTableEvaluationState];
-[CWFAssetPowerTableElector _powerTableFetched];
-[CWFAssetPowerTableElector _powerTableRequestingVotesStartDate];
-[CWFAssetPowerTableElector _powerTableSession];
-[CWFAssetPowerTableElector _powerTableSessionStartDate];
-[CWFAssetPowerTableElector _readinessTimeoutInterval];
-[CWFAssetPowerTableElector _readyToFetchLoadedPT];
-[CWFAssetPowerTableElector _readyToFetchLoadedPTCondition];
-[CWFAssetPowerTableElector _signalQueue];
-[CWFAssetPowerTableElector _votingTimeoutInterval];
-[CWFAssetPowerTableElector _waitingQueue];
-[CWFAssetPowerTableElector checkForExistingSessionAndRecover];
-[CWFAssetPowerTableElector dispatchWaitForInterfaceAddedThenBlockify:completion:];
-[CWFAssetPowerTableElector getPersistedDict];
-[CWFAssetPowerTableElector getPersistedKey:];
-[CWFAssetPowerTableElector getSession:];
-[CWFAssetPowerTableElector getSession:forKey:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationNotification:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateAborted:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateAccepted:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRejected:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingReadiness:dueInterval:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingVotes:dueInterval:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateStarting:];
-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateUninitialized];
-[CWFAssetPowerTableElector isSessionCurrentlyBlocking];
-[CWFAssetPowerTableElector performPowerTableVersionRequestWithDeadline:];
-[CWFAssetPowerTableElector performVersionFetchBlockify:];
-[CWFAssetPowerTableElector persistSession:data:forKey:];
-[CWFAssetPowerTableElector powerTableReadiness:];
-[CWFAssetPowerTableElector processTransitionToTerminalState:];
-[CWFAssetPowerTableElector removePersistedKey:];
-[CWFAssetPowerTableElector setWifiInterface:];
-[CWFAssetPowerTableElector set_apiQueue:];
-[CWFAssetPowerTableElector set_condPowerTableFetched:];
-[CWFAssetPowerTableElector set_coordinationQueue:];
-[CWFAssetPowerTableElector set_dateToBlockWaitingForDriverReload:];
-[CWFAssetPowerTableElector set_dateToFetchReloadedPowerTableForVoteAssesment:];
-[CWFAssetPowerTableElector set_distNotificationCenter:];
-[CWFAssetPowerTableElector set_driverAvailEventCondition:];
-[CWFAssetPowerTableElector set_driverAvailEventOccurred:];
-[CWFAssetPowerTableElector set_interfaceAddedEventCondition:];
-[CWFAssetPowerTableElector set_interfaceAddedEventOccurred:];
-[CWFAssetPowerTableElector set_isInternalBuild:];
-[CWFAssetPowerTableElector set_maxSessionActiveInterval:];
-[CWFAssetPowerTableElector set_pid:];
-[CWFAssetPowerTableElector set_powerTableEvaluationStartDate:];
-[CWFAssetPowerTableElector set_powerTableEvaluationState:];
-[CWFAssetPowerTableElector set_powerTableFetched:];
-[CWFAssetPowerTableElector set_powerTableRequestingVotesStartDate:];
-[CWFAssetPowerTableElector set_powerTableSession:];
-[CWFAssetPowerTableElector set_readinessTimeoutInterval:];
-[CWFAssetPowerTableElector set_readyToFetchLoadedPT:];
-[CWFAssetPowerTableElector set_readyToFetchLoadedPTCondition:];
-[CWFAssetPowerTableElector set_signalQueue:];
-[CWFAssetPowerTableElector set_votingTimeoutInterval:];
-[CWFAssetPowerTableElector set_waitingQueue:];
-[CWFAssetPowerTableElector setupInterfaceAddedAndDriverAvailMonitor];
-[CWFAssetPowerTableElector waitForInterfaceAdded:];
-[CWFAssetPowerTableElector waitForPowerTableBootedThenVoteInBlock:completion:];
-[CWFAssetPowerTableElector wifiInterface];
```
