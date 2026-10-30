# `SBBookendViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBHRootFolderCustomViewPresenting`
- 2 instance variables, 20 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBHLegibilitySettings>" _legibilitySettings;
Q _contentVisibility;
```

## Properties

```
@property (TB,?,R,N) shouldBeIndicatedInPageControl;
@property (T@"<SBIconViewQuerying>",?,R) iconViewQueryable;
@property (T@"<SBIconLocationPresenting>",?,R) iconLocationPresenter;
@property (T@"<SBIconListViewQuerying>",?,R) iconListViewQueryable;
@property (TB,?,R,N) shouldShowDoneButtonWhenEditing;
@property (TB,?,R,N) shouldShowEditMenuButtonWhenEditing;
@property (Td,?,R,N) scrollPageOffsetForButtonsInEditingMode;
@property (TB,?,N) suppressesEditingStateForListViews;
@property (TB,?,R,N) shouldObscureBackgroundWhileVisible;
@property (T@"SBIconListView",?,R,N) rootIconListView;
@property (T@"SBIconListView",?,R,N) currentIconListView;
@property (T@"NSArray",?,R,C,N) rootIconListViews;
@property (T@"UIView",?,R,N) iconZoomView;
@property (TB,?,N,GisShownInScrollView) shownInScrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBHLegibilitySettings>",&,N,V_legibilitySettings) legibilitySettings;
@property (TQ,N,V_contentVisibility) contentVisibility;
```

## Instance methods

```
-[SBBookendViewController contentVisibility];
-[SBBookendViewController loadView];
-[SBBookendViewController setContentVisibility:];
-[SBBookendViewController legibilitySettings];
-[SBBookendViewController setLegibilitySettings:];
-[SBBookendViewController shouldShowDoneButtonWhenEditing];
-[SBBookendViewController shouldBeIndicatedInPageControl];
-[SBBookendViewController shouldObscureBackgroundWhileVisible];
-[SBBookendViewController shouldShowEditMenuButtonWhenEditing];
```
