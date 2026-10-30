# `VTUIProximityTryAgainView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIButton" _dismissButton;
@"UILabel" _titleLabel;
@"VTUIStyle" _vtStyle;
@"VTPreferences" _vtPrefs;
@"VTUIProximityContainerView" _containerView;
@"NSArray" _viewConstraints;
```

## Properties

```
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"VTUIStyle",&,N,V_vtStyle) vtStyle;
@property (T@"VTPreferences",&,N,V_vtPrefs) vtPrefs;
@property (T@"VTUIProximityContainerView",&,N,V_containerView) containerView;
@property (T@"NSArray",&,N,V_viewConstraints) viewConstraints;
@property (T@"UIButton",R,N,V_dismissButton) dismissButton;
```

## Instance methods

```
-[VTUIProximityTryAgainView setContainerView:];
-[VTUIProximityTryAgainView _setupViews];
-[VTUIProximityTryAgainView setTitleLabel:];
-[VTUIProximityTryAgainView titleLabel];
-[VTUIProximityTryAgainView containerView];
-[VTUIProximityTryAgainView initWithFrame:];
-[VTUIProximityTryAgainView dismissButton];
-[VTUIProximityTryAgainView viewConstraints];
-[VTUIProximityTryAgainView setViewConstraints:];
-[VTUIProximityTryAgainView vtPrefs];
-[VTUIProximityTryAgainView vtStyle];
-[VTUIProximityTryAgainView _setupConstraintsToSize:];
-[VTUIProximityTryAgainView setVtPrefs:];
-[VTUIProximityTryAgainView setVtStyle:];
```
