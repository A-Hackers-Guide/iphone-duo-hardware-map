# `SBCaptureButtonBehaviorsResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDictionaryRepresentable`
- 4 instance variables, 8 properties, 17 instance methods, 1 class methods

## Instance variables

```
Q _prewarmIntent;
Q _launchIntent;
Q _wakeIntent;
Q _coachIntent;
```

## Properties

```
@property (TQ,R,N,V_prewarmIntent) prewarmIntent;
@property (TQ,R,N,V_launchIntent) launchIntent;
@property (TQ,R,N,V_wakeIntent) wakeIntent;
@property (TQ,R,N,V_coachIntent) coachIntent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCaptureButtonBehaviorsResponse emptyResponse];
```

## Instance methods

```
-[SBCaptureButtonBehaviorsResponse initWithDictionary:];
-[SBCaptureButtonBehaviorsResponse succinctDescriptionBuilder];
-[SBCaptureButtonBehaviorsResponse descriptionWithMultilinePrefix:];
-[SBCaptureButtonBehaviorsResponse succinctDescription];
-[SBCaptureButtonBehaviorsResponse launchIntent];
-[SBCaptureButtonBehaviorsResponse hash];
-[SBCaptureButtonBehaviorsResponse description];
-[SBCaptureButtonBehaviorsResponse isEqual:];
-[SBCaptureButtonBehaviorsResponse descriptionBuilderWithMultilinePrefix:];
-[SBCaptureButtonBehaviorsResponse dictionaryRepresentation];
-[SBCaptureButtonBehaviorsResponse coachIntent];
-[SBCaptureButtonBehaviorsResponse hasNonUnknownIntents];
-[SBCaptureButtonBehaviorsResponse initWithBehavior:context:];
-[SBCaptureButtonBehaviorsResponse initWithPrewarmIntent:launchIntent:wakeIntent:coachIntent:];
-[SBCaptureButtonBehaviorsResponse prewarmIntent];
-[SBCaptureButtonBehaviorsResponse responseByMergingResponse:];
-[SBCaptureButtonBehaviorsResponse wakeIntent];
```
