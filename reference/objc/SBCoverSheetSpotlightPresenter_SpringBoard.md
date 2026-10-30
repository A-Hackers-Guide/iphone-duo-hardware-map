# `SBCoverSheetSpotlightPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCoverSheetSpotlightViewControllerDelegate`, `SBSearchPresenterDelegate`, `SBSpotlightPresentableViewControllerDelegate`, `CSCoverSheetSpotlightPresenting`
- 6 instance variables, 6 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"<SBFCoverSheetSpotlightPresenterDelegate>" _delegate;
@"UIScrollView" _scrollView;
@"SBCoverSheetSpotlightViewController" _spotlightViewController;
@"SBSearchPresenter" _searchPresenter;
d _strength;
@"_UILegibilitySettings" _legibilitySettings;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_strength) strength;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
```

## Instance methods

```
-[SBCoverSheetSpotlightPresenter searchPresenterWillDismissSearch:animated:];
-[SBCoverSheetSpotlightPresenter searchPresenterDidPresentSearch:];
-[SBCoverSheetSpotlightPresenter spotlightPresentableViewControllerShouldDismiss:];
-[SBCoverSheetSpotlightPresenter backgroundViewForSpotlightPresentableViewController:];
-[SBCoverSheetSpotlightPresenter displayConfigurationForPresenter:];
-[SBCoverSheetSpotlightPresenter searchPresentablesForPresenter:];
-[SBCoverSheetSpotlightPresenter strength];
-[SBCoverSheetSpotlightPresenter initWithDelegate:];
-[SBCoverSheetSpotlightPresenter searchPresenterWillPresentSearch:animated:];
-[SBCoverSheetSpotlightPresenter presentSpotlightAnimated:];
-[SBCoverSheetSpotlightPresenter setStrength:];
-[SBCoverSheetSpotlightPresenter searchPresenterCanPresent:];
-[SBCoverSheetSpotlightPresenter dismissSpotlightAnimated:];
-[SBCoverSheetSpotlightPresenter scrollViewWillBeginDragging:];
-[SBCoverSheetSpotlightPresenter searchTopOffsetForSearchPresenter:];
-[SBCoverSheetSpotlightPresenter legibilitySettings];
-[SBCoverSheetSpotlightPresenter searchPresenterDidDismissSearch:];
-[SBCoverSheetSpotlightPresenter setLegibilitySettings:];
-[SBCoverSheetSpotlightPresenter scrollViewWillEndDragging:withVelocity:];
-[SBCoverSheetSpotlightPresenter scrollViewDidScroll:];
-[SBCoverSheetSpotlightPresenter spotlightViewController];
-[SBCoverSheetSpotlightPresenter coordinateStateWithSourceSpotlightPresenter:];
-[SBCoverSheetSpotlightPresenter displayConfigurationForView:];
-[SBCoverSheetSpotlightPresenter _setUpStartingScrollOffsetWithScrollView:];
-[SBCoverSheetSpotlightPresenter coverSheetSpotlightViewControllerAddContentView:];
-[SBCoverSheetSpotlightPresenter coverSheetSpotlightViewControllerRemoveContentView:];
-[SBCoverSheetSpotlightPresenter coverSheetSpotlightViewControllerShouldDismiss:animated:];
-[SBCoverSheetSpotlightPresenter dismissSpotlightAnimated:completion:];
-[SBCoverSheetSpotlightPresenter isSpotlightPresented];
```
