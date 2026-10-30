# `BKSHIDEventBaseAttributes`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSProtobufSerializable`, `NSCopying`, `BSDescriptionStreamable`
- 7 instance variables, 13 properties, 25 instance methods, 5 class methods

## Instance variables

```
@"BKSHIDEventSimpleProvenance" _simpleProvenance;
S _options;
i _source;
@"BKSHIDEventAuthenticationMessage" _authenticationMessage;
@"BKSHIDEventDeferringEnvironment" _environment;
@"BKSHIDEventDisplay" _display;
@"BKSHIDEventDeferringToken" _token;
```

## Properties

```
@property (T@"<BKSHIDEventProvenance>",&,N) provenance;
@property (T@"BKSHIDEventDeferringChangeBasis",R,N) changeBasis;
@property (T@"BKSHIDEventAuthenticationMessage",&,N,V_authenticationMessage) authenticationMessage;
@property (T@"BKSHIDEventDeferringEnvironment",&,N,V_environment) environment;
@property (T@"BKSHIDEventDisplay",&,N,V_display) display;
@property (T@"BKSHIDEventDeferringToken",&,N,V_token) token;
@property (Ti,N,V_source) source;
@property (TS,N,V_options) options;
@property (TI,R,N) contextID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventBaseAttributes protobufSchema];
+[BKSHIDEventBaseAttributes deserializeFromBytes:byteCount:];
+[BKSHIDEventBaseAttributes baseAttributesFromProvider:];
+[BKSHIDEventBaseAttributes _classForAttributeType:];
+[BKSHIDEventBaseAttributes _eventAttributeType];
```

## Instance methods

```
-[BKSHIDEventBaseAttributes serializedData];
-[BKSHIDEventBaseAttributes setDisplay:];
-[BKSHIDEventBaseAttributes provenance];
-[BKSHIDEventBaseAttributes authenticationMessage];
-[BKSHIDEventBaseAttributes setEnvironment:];
-[BKSHIDEventBaseAttributes display];
-[BKSHIDEventBaseAttributes setOptions:];
-[BKSHIDEventBaseAttributes succinctDescriptionBuilder];
-[BKSHIDEventBaseAttributes appendDescriptionToFormatter:];
-[BKSHIDEventBaseAttributes setAuthenticationMessage:];
-[BKSHIDEventBaseAttributes descriptionWithMultilinePrefix:];
-[BKSHIDEventBaseAttributes setSource:];
-[BKSHIDEventBaseAttributes succinctDescription];
-[BKSHIDEventBaseAttributes description];
-[BKSHIDEventBaseAttributes token];
-[BKSHIDEventBaseAttributes setToken:];
-[BKSHIDEventBaseAttributes options];
-[BKSHIDEventBaseAttributes contextID];
-[BKSHIDEventBaseAttributes copyWithZone:];
-[BKSHIDEventBaseAttributes setProvenance:];
-[BKSHIDEventBaseAttributes isEqual:];
-[BKSHIDEventBaseAttributes source];
-[BKSHIDEventBaseAttributes environment];
-[BKSHIDEventBaseAttributes changeBasis];
-[BKSHIDEventBaseAttributes descriptionBuilderWithMultilinePrefix:];
```
