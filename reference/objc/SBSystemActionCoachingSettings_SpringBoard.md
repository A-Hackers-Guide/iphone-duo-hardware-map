# `SBSystemActionCoachingSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 12 instance variables, 12 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _policyClassName;
@"SBSystemActionTrackPreviewsCoachingPolicySettings" _trackPreviewsPolicySettings;
@"SBSystemActionPressWithinTimeIntervalCoachingPolicySettings" _pressWithinTimeIntervalPolicySettings;
d _dimmingAlpha;
d _coachingButtonShadowOpacity;
d _coachingButtonShadowRadius;
d _coachingLabelShadowOpacity;
d _coachingLabelShadowRadius;
@"SBFFluidBehaviorSettings" _presentationSettings;
@"SBFFluidBehaviorSettings" _expansionSettings;
@"SBFFluidBehaviorSettings" _contractionSettings;
@"SBFFluidBehaviorSettings" _dismissalSettings;
```

## Properties

```
@property (T@"NSString",&,N,V_policyClassName) policyClassName;
@property (T@"SBSystemActionTrackPreviewsCoachingPolicySettings",&,N,V_trackPreviewsPolicySettings) trackPreviewsPolicySettings;
@property (T@"SBSystemActionPressWithinTimeIntervalCoachingPolicySettings",&,N,V_pressWithinTimeIntervalPolicySettings) pressWithinTimeIntervalPolicySettings;
@property (Td,N,V_dimmingAlpha) dimmingAlpha;
@property (Td,N,V_coachingButtonShadowOpacity) coachingButtonShadowOpacity;
@property (Td,N,V_coachingButtonShadowRadius) coachingButtonShadowRadius;
@property (Td,N,V_coachingLabelShadowOpacity) coachingLabelShadowOpacity;
@property (Td,N,V_coachingLabelShadowRadius) coachingLabelShadowRadius;
@property (T@"SBFFluidBehaviorSettings",&,N,V_presentationSettings) presentationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_expansionSettings) expansionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_contractionSettings) contractionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_dismissalSettings) dismissalSettings;
```

## Class methods

```
+[SBSystemActionCoachingSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemActionCoachingSettings setDefaultValues];
-[SBSystemActionCoachingSettings dimmingAlpha];
-[SBSystemActionCoachingSettings setDimmingAlpha:];
-[SBSystemActionCoachingSettings setTrackPreviewsPolicySettings:];
-[SBSystemActionCoachingSettings policyClassName];
-[SBSystemActionCoachingSettings setCoachingButtonShadowOpacity:];
-[SBSystemActionCoachingSettings coachingButtonShadowOpacity];
-[SBSystemActionCoachingSettings coachingButtonShadowRadius];
-[SBSystemActionCoachingSettings coachingLabelShadowOpacity];
-[SBSystemActionCoachingSettings coachingLabelShadowRadius];
-[SBSystemActionCoachingSettings contractionSettings];
-[SBSystemActionCoachingSettings dismissalSettings];
-[SBSystemActionCoachingSettings expansionSettings];
-[SBSystemActionCoachingSettings presentationSettings];
-[SBSystemActionCoachingSettings pressWithinTimeIntervalPolicySettings];
-[SBSystemActionCoachingSettings setCoachingButtonShadowRadius:];
-[SBSystemActionCoachingSettings setCoachingLabelShadowOpacity:];
-[SBSystemActionCoachingSettings setCoachingLabelShadowRadius:];
-[SBSystemActionCoachingSettings setContractionSettings:];
-[SBSystemActionCoachingSettings setDismissalSettings:];
-[SBSystemActionCoachingSettings setExpansionSettings:];
-[SBSystemActionCoachingSettings setPolicyClassName:];
-[SBSystemActionCoachingSettings setPresentationSettings:];
-[SBSystemActionCoachingSettings setPressWithinTimeIntervalPolicySettings:];
-[SBSystemActionCoachingSettings trackPreviewsPolicySettings];
```
