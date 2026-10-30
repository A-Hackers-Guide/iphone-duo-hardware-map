# `CWFKnownNetworkPreparer`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _maxResults;
@"NSArray" _profiles;
```

## Properties

```
@property (T@"NSArray",&,N,V_profiles) profiles;
@property (TQ,N,V_maxResults) maxResults;
```

## Instance methods

```
-[CWFKnownNetworkPreparer maxResults];
-[CWFKnownNetworkPreparer setMaxResults:];
-[CWFKnownNetworkPreparer profiles];
-[CWFKnownNetworkPreparer setProfiles:];
-[CWFKnownNetworkPreparer _filterForPrimaryHomeNetworkProfile:];
-[CWFKnownNetworkPreparer _filterProfilesForHomeNetworksExceedingMaximumDistance:];
-[CWFKnownNetworkPreparer _homeNetworkComparator];
-[CWFKnownNetworkPreparer _homeNetworkFilter];
-[CWFKnownNetworkPreparer _lastJoinedComparator];
-[CWFKnownNetworkPreparer _localNetworkFilter];
-[CWFKnownNetworkPreparer _networkProfileUsageComparator];
-[CWFKnownNetworkPreparer _presentationSortComparator];
-[CWFKnownNetworkPreparer _removeProfilesAtSimilarLocations:];
-[CWFKnownNetworkPreparer _similarLocationComparator];
-[CWFKnownNetworkPreparer initWithNetworkProfiles:];
-[CWFKnownNetworkPreparer localNetworkPromptProfiles];
-[CWFKnownNetworkPreparer prepareLocalNetworkProfilesForPresentation:];
-[CWFKnownNetworkPreparer profilesContainsHomeProfile:];
```
