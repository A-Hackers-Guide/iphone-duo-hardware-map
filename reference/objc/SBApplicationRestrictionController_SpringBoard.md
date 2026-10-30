# `SBApplicationRestrictionController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `STTelephonyStateObserver`
- 15 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"<SBApplicationRestrictionDataSource>" _dataSource;
@"STTelephonyStateProvider" _telephonyStateProvider;
@"NSHashTable" _observers;
@"NSMutableDictionary" _tagValidityMap;
@"NSMutableDictionary" _validTagsByIdentifier;
^{MGNotificationTokenStruct=} _tagsNotificationToken;
@"NSMutableSet" _enabledTags;
@"NSMutableDictionary" _ratingRanksByIdentifier;
@"NSSet" _restrictedIdentifiers;
@"NSMutableSet" _appRestrictedIdentifiers;
@"NSMutableSet" _partiallyRestrictedIdentifiers;
@"SBApplicationDefaults" _applicationDefaults;
B _showInternalApps;
B _isAppAllowlistActiveAndTransient;
B _canPostRestrictionState;
```

## Properties

```
@property (TB,R,N,GisAllowlistActiveAndTransient) allowlistActiveAndTransient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBApplicationRestrictionController isAllowlistActiveAndTransient];
```

## Instance methods

```
-[SBApplicationRestrictionController initWithDataSource:];
-[SBApplicationRestrictionController removeObserver:];
-[SBApplicationRestrictionController init];
-[SBApplicationRestrictionController dealloc];
-[SBApplicationRestrictionController carrierBundleInfoDidChangeForStateProvider:slot:];
-[SBApplicationRestrictionController addObserver:];
-[SBApplicationRestrictionController allAllowedAppBundleIdentifiers];
-[SBApplicationRestrictionController allRestrictedAppBundleIdentifiers];
-[SBApplicationRestrictionController beginPostingChanges];
-[SBApplicationRestrictionController initWithDataSource:telephonyStateProvider:];
-[SBApplicationRestrictionController isAllowlistActiveAndTransient];
-[SBApplicationRestrictionController isApplicationIdentifierRestricted:];
-[SBApplicationRestrictionController isApplicationIdentifierRestrictedForLaunchTransitions:];
-[SBApplicationRestrictionController noteApplicationIdentifiersDidChangeWithAdded:replaced:removed:updated:];
-[SBApplicationRestrictionController noteRestrictionsMayHaveChanged];
-[SBApplicationRestrictionController noteVisibilityOverridesDidChange];
```
