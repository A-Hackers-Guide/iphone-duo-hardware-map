# `SBCaptureButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDictionaryRepresentable`
- 4 instance variables, 8 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"SBCaptureButtonContext" _context;
@"SBCaptureButtonBehaviorsResponse" _response;
@"NSArray" _responseLogs;
Q _intention;
```

## Properties

```
@property (T@"SBCaptureButtonContext",R,N,V_context) context;
@property (T@"SBCaptureButtonBehaviorsResponse",R,N,V_response) response;
@property (T@"NSArray",R,C,N,V_responseLogs) responseLogs;
@property (TQ,N,V_intention) intention;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCaptureButtonInteraction fromString:];
```

## Instance methods

```
-[SBCaptureButtonInteraction initWithDictionary:];
-[SBCaptureButtonInteraction succinctDescriptionBuilder];
-[SBCaptureButtonInteraction descriptionWithMultilinePrefix:];
-[SBCaptureButtonInteraction succinctDescription];
-[SBCaptureButtonInteraction launched];
-[SBCaptureButtonInteraction hash];
-[SBCaptureButtonInteraction description];
-[SBCaptureButtonInteraction context];
-[SBCaptureButtonInteraction isEqual:];
-[SBCaptureButtonInteraction response];
-[SBCaptureButtonInteraction descriptionBuilderWithMultilinePrefix:];
-[SBCaptureButtonInteraction dictionaryRepresentation];
-[SBCaptureButtonInteraction mitigated];
-[SBCaptureButtonInteraction logToCoreAnalytics];
-[SBCaptureButtonInteraction JSONString];
-[SBCaptureButtonInteraction intention];
-[SBCaptureButtonInteraction _coreAnalyticsDictionaryRepresentation];
-[SBCaptureButtonInteraction initWithContext:response:responseLogs:];
-[SBCaptureButtonInteraction launchIntentDecidingBehavior];
-[SBCaptureButtonInteraction responseLogs];
-[SBCaptureButtonInteraction setIntention:];
```
