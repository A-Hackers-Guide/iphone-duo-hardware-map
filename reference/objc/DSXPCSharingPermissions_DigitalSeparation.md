# `DSXPCSharingPermissions`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 7 properties, 39 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _permissionsLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionLock;
@"NSMutableDictionary" _pendingCompletions;
@"NSDictionary" _sharedResourcesBySource;
@"NSMutableOrderedSet" _people;
@"NSXPCConnection" _xpcConnection;
Q _fetchCompletedTime;
@"NSError" _cachedFetchError;
@"DSMe" _me;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_sharedResourcesBySource) sharedResourcesBySource;
@property (T@"NSMutableOrderedSet",&,N,V_people) people;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TQ,V_fetchCompletedTime) fetchCompletedTime;
@property (T@"NSError",&,N,V_cachedFetchError) cachedFetchError;
@property (T@"DSMe",&,V_me) me;
@property (T@"NSArray",R,C,N) allPeople;
```

## Class methods

```
+[DSXPCSharingPermissions sharedInstance];
+[DSXPCSharingPermissions interface];
```

## Instance methods

```
-[DSXPCSharingPermissions me];
-[DSXPCSharingPermissions setPeople:];
-[DSXPCSharingPermissions people];
-[DSXPCSharingPermissions init];
-[DSXPCSharingPermissions setXpcConnection:];
-[DSXPCSharingPermissions setMe:];
-[DSXPCSharingPermissions dealloc];
-[DSXPCSharingPermissions xpcConnection];
-[DSXPCSharingPermissions allPeople];
-[DSXPCSharingPermissions fetchSharingWithCompletion:];
-[DSXPCSharingPermissions makeSharingPeopleWithResources:];
-[DSXPCSharingPermissions _addLinkedSharingToPerson:];
-[DSXPCSharingPermissions _addParticipationFromResource:fromSource:toModel:strictlyMatchingContacts:];
-[DSXPCSharingPermissions _consumePendingCompletion:];
-[DSXPCSharingPermissions _failAllPendingOperationsWithError:];
-[DSXPCSharingPermissions _fetchSharingWithCompletion:];
-[DSXPCSharingPermissions _registerPendingCompletion:];
-[DSXPCSharingPermissions _sharingPeopleForContacts:completion:];
-[DSXPCSharingPermissions _sharingPeopleForIdentities:completion:];
-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:];
-[DSXPCSharingPermissions cachedFetchError];
-[DSXPCSharingPermissions deviceOwnerRoleForSharedResource:];
-[DSXPCSharingPermissions fetchCompletedTime];
-[DSXPCSharingPermissions isFetchNeeded];
-[DSXPCSharingPermissions makeSharingPeople];
-[DSXPCSharingPermissions remoteProxyForCompletionToken:];
-[DSXPCSharingPermissions requestImmediateFetch];
-[DSXPCSharingPermissions safetycheckdConnectionWithFailureHandlers:];
-[DSXPCSharingPermissions setCachedFetchError:];
-[DSXPCSharingPermissions setDSMe:];
-[DSXPCSharingPermissions setFailureHandlersForConnection:];
-[DSXPCSharingPermissions setFetchCompletedTime:];
-[DSXPCSharingPermissions setSharedResourcesBySource:];
-[DSXPCSharingPermissions setSharing:];
-[DSXPCSharingPermissions sharedResourcesBySource];
-[DSXPCSharingPermissions sharingPeopleForContacts:completion:];
-[DSXPCSharingPermissions sharingPeopleForIdentities:completion:];
-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:];
-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:];
```
