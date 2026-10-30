# `SBMainDisplayLayoutState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBLayoutState`
- 17 instance variables, 24 properties, 48 instance methods, 1 class methods

## Instance variables

```
@"SBAppLayout" _cachedAppLayoutIfAny;
@"NSDictionary" _cachedLayoutAttributesIfAny;
@"SBAppLayout" _cachedFloatingAppLayoutIfAny;
@"NSDictionary" _elementIdentifiersToLayoutAttributes;
B _floatingSwitcherVisible;
B _centerEntityModal;
B _isDisplayExternal;
q _spaceConfiguration;
q _floatingConfiguration;
q _centerConfiguration;
q _peekConfiguration;
@"SBAppExposeBundleIdentifierState" _appExposeBundleIdentifierState;
q _windowPickerRole;
q _displayOrdinal;
@"NSString" _continuousExposeIdentifier;
@"SBSplitPIPContext" _splitPIPContext;
@"SBUnlockedEnvironmentState" _unlockedEnvironmentState;
```

## Properties

```
@property (TB,R,N) effectivelyRepresentsHomeScreen;
@property (T@"NSDictionary",R,C,N) displayItemLayoutAttributesMap;
@property (TB,R,N,V_isDisplayExternal) isDisplayExternal;
@property (T@"SBUnlockedEnvironmentState",R,N,V_unlockedEnvironmentState) unlockedEnvironmentState;
@property (T@"SBSplitPIPContext",&,N,V_splitPIPContext) splitPIPContext;
@property (Tq,R,N,V_spaceConfiguration) spaceConfiguration;
@property (TB,R,N) isFullScreen;
@property (TB,R,N) isSplitView;
@property (T@"NSDictionary",R,C,N,V_elementIdentifiersToLayoutAttributes) elementIdentifiersToLayoutAttributes;
@property (Tq,R,N,V_floatingConfiguration) floatingConfiguration;
@property (Tq,R,N,V_centerConfiguration) centerConfiguration;
@property (Tq,R,N,V_peekConfiguration) peekConfiguration;
@property (Tq,R,N) unlockedEnvironmentMode;
@property (TB,R,N,GisHomeScreenVisible) homeScreenVisible;
@property (TB,R,N,GisAppSwitcherVisible) appSwitcherVisible;
@property (TB,R,N,GisApplicationVisible) applicationVisible;
@property (Tq,R,N) screenRegionForHomeScreen;
@property (T@"NSString",R,N) bundleIDShowingAppExpose;
@property (T@"SBAppExposeBundleIdentifierState",R,N,V_appExposeBundleIdentifierState) appExposeBundleIdentifierState;
@property (TB,R,N,GisFloatingSwitcherVisible,V_floatingSwitcherVisible) floatingSwitcherVisible;
@property (TB,R,N,GisCenterEntityModal,V_centerEntityModal) centerEntityModal;
@property (Tq,R,N,V_windowPickerRole) windowPickerRole;
@property (Tq,R,N,V_displayOrdinal) displayOrdinal;
@property (T@"NSString",R,C,N,V_continuousExposeIdentifier) continuousExposeIdentifier;
```

## Class methods

```
+[SBMainDisplayLayoutState _elementIdentifiersToLayoutAttributesForElements:spaceConfiguration:];
```

## Instance methods

```
-[SBMainDisplayLayoutState displayOrdinal];
-[SBMainDisplayLayoutState continuousExposeIdentifier];
-[SBMainDisplayLayoutState centerConfiguration];
-[SBMainDisplayLayoutState floatingConfiguration];
-[SBMainDisplayLayoutState isFullScreen];
-[SBMainDisplayLayoutState isCenterEntityModal];
-[SBMainDisplayLayoutState _initWithLayoutElements:interfaceOrientation:interfaceOrientationByLayoutElement:spaceConfiguration:elementIdentifiersToLayoutAttributes:floatingConfiguration:unlockedEnvironmentMode:floatingSwitcherVisible:centerConfiguration:centerEntityModal:peekConfiguration:appExposeBundleIdentifierState:windowPickerRole:displayOrdinal:isDisplayExternal:splitPIPContext:];
-[SBMainDisplayLayoutState screenRegionForHomeScreen];
-[SBMainDisplayLayoutState invalidateAppLayout];
-[SBMainDisplayLayoutState _updateSizingPoliciesForLayoutElements:];
-[SBMainDisplayLayoutState appLayout];
-[SBMainDisplayLayoutState _initWithLayoutElements:interfaceOrientation:interfaceOrientationByLayoutElement:spaceConfiguration:elementIdentifiersToLayoutAttributes:floatingConfiguration:unlockedEnvironmentState:floatingSwitcherVisible:centerConfiguration:centerEntityModal:peekConfiguration:appExposeBundleIdentifierState:windowPickerRole:displayOrdinal:isDisplayExternal:splitPIPContext:];
-[SBMainDisplayLayoutState isApplicationVisible];
-[SBMainDisplayLayoutState _initWithLayoutState:];
-[SBMainDisplayLayoutState unlockedEnvironmentState];
-[SBMainDisplayLayoutState bundleIDShowingAppExpose];
-[SBMainDisplayLayoutState invalidateFloatingAppLayout];
-[SBMainDisplayLayoutState _setLayoutAttributes:forLayoutElement:];
-[SBMainDisplayLayoutState splitPIPContext];
-[SBMainDisplayLayoutState _layoutAttributesForElementWithIdentifier:];
-[SBMainDisplayLayoutState isHomeScreenVisible];
-[SBMainDisplayLayoutState isDisplayExternal];
-[SBMainDisplayLayoutState isAppSwitcherVisible];
-[SBMainDisplayLayoutState displayItemLayoutAttributesMap];
-[SBMainDisplayLayoutState setInterfaceOrientationByLayoutElementIdentifier:];
-[SBMainDisplayLayoutState spaceConfiguration];
-[SBMainDisplayLayoutState layoutAttributesForElement:];
-[SBMainDisplayLayoutState layoutAttributesMap];
-[SBMainDisplayLayoutState effectivelyRepresentsHomeScreen];
-[SBMainDisplayLayoutState setSplitPIPContext:];
-[SBMainDisplayLayoutState _applyElementInterfaceOrientationsToLayoutAttributes];
-[SBMainDisplayLayoutState isSplitView];
-[SBMainDisplayLayoutState _initWithLayoutElements:interfaceOrientation:interfaceOrientationByLayoutElement:spaceConfiguration:floatingConfiguration:unlockedEnvironmentMode:floatingSwitcherVisible:centerConfiguration:centerEntityModal:peekConfiguration:appExposeBundleIdentifierState:windowPickerRole:displayOrdinal:isDisplayExternal:splitPIPContext:];
-[SBMainDisplayLayoutState hash];
-[SBMainDisplayLayoutState unlockedEnvironmentMode];
-[SBMainDisplayLayoutState isFloatingSwitcherVisible];
-[SBMainDisplayLayoutState description];
-[SBMainDisplayLayoutState peekConfiguration];
-[SBMainDisplayLayoutState _initWithLayoutElements:spaceConfiguration:elementIdentifiersToLayoutAttributes:floatingConfiguration:unlockedEnvironmentState:floatingSwitcherVisible:centerConfiguration:centerEntityModal:peekConfiguration:appExposeBundleIdentifierState:windowPickerRole:displayOrdinal:isDisplayExternal:splitPIPContext:];
-[SBMainDisplayLayoutState appExposeBundleIdentifierState];
-[SBMainDisplayLayoutState _initWithLayoutElements:spaceConfiguration:floatingConfiguration:unlockedEnvironmentMode:floatingSwitcherVisible:centerConfiguration:centerEntityModal:peekConfiguration:appExposeBundleIdentifierState:windowPickerRole:displayOrdinal:isDisplayExternal:splitPIPContext:];
-[SBMainDisplayLayoutState isEqual:];
-[SBMainDisplayLayoutState _initWithLayoutElements:interfaceOrientation:interfaceOrientationByLayoutElement:];
-[SBMainDisplayLayoutState elementIdentifiersToLayoutAttributes];
-[SBMainDisplayLayoutState floatingAppLayout];
-[SBMainDisplayLayoutState _defaultInterfaceOrientation];
-[SBMainDisplayLayoutState windowPickerRole];
-[SBMainDisplayLayoutState descriptionBuilderWithMultilinePrefix:];
```
