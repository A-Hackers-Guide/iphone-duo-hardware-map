# `SBRecentAppLayouts`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationRestrictionObserver`
- 16 instance variables, 6 properties, 55 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _allRecents;
@"NSMutableArray" _unhiddenRecents;
@"NSDictionary" _allRecentsForBundleIdentifiers;
@"NSDictionary" _unhiddenRecentsForBundleIdentifiers;
@"NSDictionary" _allRecentDisplayItemsForBundleIdentifiers;
@"NSDictionary" _unhiddenRecentDisplayItemsForBundleIdentifiers;
@"NSMutableDictionary" _allowHiddenAppAssertions;
@"SBAppSwitcherDefaults" _defaults;
@"SBHIconRepository" _iconRepository;
@"SBApplicationController" _applicationController;
@"SBApplicationPlaceholderController" _placeholderController;
@"SBSceneManager" _sceneManager;
@"SBRecentAppLayoutsPersister" _persister;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"<SBRecentAppLayoutsDelegate>" _delegate;
@"<SBDisplayItemLayoutAttributesProviding>" _layoutAttributesProvider;
```

## Properties

```
@property (T@"<SBRecentAppLayoutsDelegate>",R,W,N,V_delegate) delegate;
@property (T@"<SBDisplayItemLayoutAttributesProviding>",R,N,V_layoutAttributesProvider) layoutAttributesProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBRecentAppLayouts allowedHiddenApplicationBundleIdentifiers];
```

## Instance methods

```
-[SBRecentAppLayouts applicationRestrictionController:didUpdateVisibleTags:hiddenTags:];
-[SBRecentAppLayouts addAppLayout:atIndex:];
-[SBRecentAppLayouts initWithDelegate:];
-[SBRecentAppLayouts _persistSoon];
-[SBRecentAppLayouts _addAllAppsToModel];
-[SBRecentAppLayouts _installedApplicationsDidChange:];
-[SBRecentAppLayouts _recentDisplayItemsFromLegacyPrefs];
-[SBRecentAppLayouts _changeDescriptionForFilteringAppLayouts:withDisplayItemTest:];
-[SBRecentAppLayouts _migrateDisplayItemIfNeeded:withApplicationSceneIdentityCreator:];
-[SBRecentAppLayouts _filterRestrictedUnsupportedAndInvalidAppsFromRecents];
-[SBRecentAppLayouts _removeAllowHiddenAppAssertionForBundleIdentifier:requestIdentifier:];
-[SBRecentAppLayouts _ppt_loadStashedModel];
-[SBRecentAppLayouts _nextInteractionTimeInOrientation:];
-[SBRecentAppLayouts _acquireAllowHiddenAppAssertionForBundleIdentifier:reason:];
-[SBRecentAppLayouts _setUpStashedModelSettingsOutlets];
-[SBRecentAppLayouts _isExistingSceneIdentifierValidForClaimedMultiwindowSupportInDisplayItem:];
-[SBRecentAppLayouts mostRecentAppLayoutIncludingHiddenAppLayouts:passingTest:];
-[SBRecentAppLayouts remove:];
-[SBRecentAppLayouts dealloc];
-[SBRecentAppLayouts recentsIncludingHiddenAppLayouts:];
-[SBRecentAppLayouts _loadStashedModelAtPath:];
-[SBRecentAppLayouts _isApplicationSupported:];
-[SBRecentAppLayouts initWithDelegate:persister:layoutAttributesProvider:];
-[SBRecentAppLayouts _iconVisibilityDidChange:];
-[SBRecentAppLayouts _ppt_setModel:];
-[SBRecentAppLayouts _saveRecents];
-[SBRecentAppLayouts recentsForBundleIdentifier:includingHiddenAppLayouts:];
-[SBRecentAppLayouts _changeDescriptionForFilteringRestrictedOrUnsupportedAppsFromAppLayouts:];
-[SBRecentAppLayouts layoutAttributesProvider];
-[SBRecentAppLayouts displayItemsForSplitIdentifier:];
-[SBRecentAppLayouts _stashModelToPath:];
-[SBRecentAppLayouts _validateAndUpdateRecents:];
-[SBRecentAppLayouts _ignoresAppHiddenForDisplayItem:];
-[SBRecentAppLayouts _setRecents:notifyForChangeDescription:];
-[SBRecentAppLayouts _lastInteractionTimeInOrientation:];
-[SBRecentAppLayouts addToFront:];
-[SBRecentAppLayouts delegate];
-[SBRecentAppLayouts _legacyAppLayoutsForDisplayItems:layoutRolesMapping:];
-[SBRecentAppLayouts _addAllowHiddenAppAssertionForBundleIdentifier:requestIdentifier:];
-[SBRecentAppLayouts _displayItemLayoutRolesFromLegacyPrefsForLoadedDisplayItems:];
-[SBRecentAppLayouts _initializeRecents];
-[SBRecentAppLayouts _isDisplayItemRestrictedOrUnsupported:];
-[SBRecentAppLayouts _persistSynchronously];
-[SBRecentAppLayouts removeAppLayouts:];
-[SBRecentAppLayouts _filterRestrictedOrUnsupportedAppsFromRecents];
-[SBRecentAppLayouts recentDisplayItemsForBundleIdentifier:includingHiddenAppLayouts:];
-[SBRecentAppLayouts _ppt_currentModel];
-[SBRecentAppLayouts _transitionContextRepresentsAmbiguousLaunch:forApplicationSceneEntity:switcherController:outEntities:];
-[SBRecentAppLayouts _shouldAllowMultipleDisplayItemsForApplication:];
-[SBRecentAppLayouts addAppLayout:afterAppLayout:];
-[SBRecentAppLayouts _legacyAppLayoutForItem:layoutRole:];
-[SBRecentAppLayouts replaceAppLayout:withAppLayout:];
-[SBRecentAppLayouts _changeDescriptionForFilteringRestrictedUnsupportedAndInvalidAppsFromAppLayouts:];
-[SBRecentAppLayouts hide:];
-[SBRecentAppLayouts _recentsFromPrefs];
```
