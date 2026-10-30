# `CLEEDFeedbackRequest`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLEEDRequest`
- 6 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _callRelatedToEmergency;
q _feedbackVersion;
@"NSNumber" _callerResponsive;
q _callTrigger;
q _callReason;
@"NSNumber" _respondersDispatched;
```

## Properties

```
@property (Tq,N,V_feedbackVersion) feedbackVersion;
@property (TB,N,V_callRelatedToEmergency) callRelatedToEmergency;
@property (T@"NSNumber",N,V_callerResponsive) callerResponsive;
@property (Tq,N,V_callTrigger) callTrigger;
@property (Tq,N,V_callReason) callReason;
@property (T@"NSNumber",N,V_respondersDispatched) respondersDispatched;
```

## Instance methods

```
-[CLEEDFeedbackRequest initWithDictionary:error:];
-[CLEEDFeedbackRequest dealloc];
-[CLEEDFeedbackRequest description];
-[CLEEDFeedbackRequest feedbackVersion];
-[CLEEDFeedbackRequest setCallTrigger:];
-[CLEEDFeedbackRequest callReason];
-[CLEEDFeedbackRequest callRelatedToEmergency];
-[CLEEDFeedbackRequest callTrigger];
-[CLEEDFeedbackRequest callerResponsive];
-[CLEEDFeedbackRequest getBooleanAsNumberFromDictionary:key:];
-[CLEEDFeedbackRequest getIntegerAsNumberFromDictionary:key:];
-[CLEEDFeedbackRequest getRequestDict];
-[CLEEDFeedbackRequest initWithDictionary:decryptedRequestData:baseURL:error:];
-[CLEEDFeedbackRequest initWithID:psapID:partnerID:geofenceID:requestDate:state:feedbackVersion:callRelatedToEmergency:callerResponsive:callTrigger:callReason:respondersDispatched:];
-[CLEEDFeedbackRequest respondersDispatched];
-[CLEEDFeedbackRequest setCallReason:];
-[CLEEDFeedbackRequest setCallRelatedToEmergency:];
-[CLEEDFeedbackRequest setCallerResponsive:];
-[CLEEDFeedbackRequest setFeedbackVersion:];
-[CLEEDFeedbackRequest setRespondersDispatched:];
```
