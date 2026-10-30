# `ACCAnalyticsLogger`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLSessionDelegate`
- 19 instance variables, 14 properties, 29 instance methods, 4 class methods

## Instance variables

```
@"ACCAnalyticsLoggerSQLiteStore" _database;
@"NSURL" _figaroUploadURL;
@"NSString" _figaroTopicName;
@"NSURL" _figaroBagURL;
@"NSObject<OS_dispatch_queue>" _queue;
q _secondsBetweenUploads;
q _secondsBetweenUploadError;
@"NSDictionary" _metricsBase;
@"NSArray" _blacklistedFields;
@"NSArray" _blacklistedEvents;
b1 _allowInsecureFigaroCert;
b1 _disableLogging;
b1 _disableUploads;
b1 _ignoreServersMessagesTellingUsToGoAway;
i _user;
@"NSMutableArray" _pluginEventsBeforeFirstUnlock;
@"NSMutableArray" _accessorydEventsBeforeFirstUnlock;
@"NSLock" _eventCacheLock;
@"NSObject<OS_dispatch_queue>" _loggingQueue;
```

## Properties

```
@property (Ti,N,V_user) user;
@property (T@"NSMutableArray",&,N,V_pluginEventsBeforeFirstUnlock) pluginEventsBeforeFirstUnlock;
@property (T@"NSMutableArray",&,N,V_accessorydEventsBeforeFirstUnlock) accessorydEventsBeforeFirstUnlock;
@property (T@"NSLock",&,N,V_eventCacheLock) eventCacheLock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_loggingQueue) loggingQueue;
@property (T@"NSURL",R,V_figaroUploadURL) figaroUploadURL;
@property (T@"NSString",R,V_figaroTopicName) figaroTopicName;
@property (T@"NSURL",R,V_figaroBagURL) figaroBagURL;
@property (TB,R) allowsInsecureFigaroCert;
@property (TB) ignoreServerDisablingMessages;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ACCAnalyticsLogger fuzzyDaysSinceDate:];
+[ACCAnalyticsLogger addBuiltInFieldsToEvent:];
+[ACCAnalyticsLogger databasePathForUser:];
+[ACCAnalyticsLogger loggerForUser:];
```

## Instance methods

```
-[ACCAnalyticsLogger setLoggingQueue:];
-[ACCAnalyticsLogger URLSession:didReceiveChallenge:completionHandler:];
-[ACCAnalyticsLogger setUser:];
-[ACCAnalyticsLogger user];
-[ACCAnalyticsLogger setDateProperty:forKey:];
-[ACCAnalyticsLogger loggingQueue];
-[ACCAnalyticsLogger datePropertyForKey:];
-[ACCAnalyticsLogger initForUser:];
-[ACCAnalyticsLogger figaroTopicName];
-[ACCAnalyticsLogger figaroUploadURL];
-[ACCAnalyticsLogger _logEventNamed:withAttributes:];
-[ACCAnalyticsLogger _onQueuePostJSON:error:httpStatusCode:];
-[ACCAnalyticsLogger accessorydEventsBeforeFirstUnlock];
-[ACCAnalyticsLogger allowsInsecureFigaroCert];
-[ACCAnalyticsLogger eventCacheLock];
-[ACCAnalyticsLogger eventDictForEventName:withAttributes:];
-[ACCAnalyticsLogger eventDictWithBlacklistedFieldsStrippedFrom:];
-[ACCAnalyticsLogger figaroBagURL];
-[ACCAnalyticsLogger forceUploadWithError:httpStatusCode:];
-[ACCAnalyticsLogger getLoggingJSON:error:];
-[ACCAnalyticsLogger ignoreServerDisablingMessages];
-[ACCAnalyticsLogger logEventNamed:withAttributes:];
-[ACCAnalyticsLogger pluginEventsBeforeFirstUnlock];
-[ACCAnalyticsLogger resetUploadDateAndClearDBEntries:dueToError:];
-[ACCAnalyticsLogger setAccessorydEventsBeforeFirstUnlock:];
-[ACCAnalyticsLogger setAllowsInsecureFigaroCert:];
-[ACCAnalyticsLogger setEventCacheLock:];
-[ACCAnalyticsLogger setIgnoreServerDisablingMessages:];
-[ACCAnalyticsLogger setPluginEventsBeforeFirstUnlock:];
```
