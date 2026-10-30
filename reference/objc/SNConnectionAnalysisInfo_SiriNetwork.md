# `SNConnectionAnalysisInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _wwanPreferred;
i _interfaceIndex;
@"NSURL" _connectionURL;
@"NSNumber" _sendBufferSize;
@"SNConnectionType" _connectionType;
@"NSString" _policyId;
```

## Properties

```
@property (T@"NSURL",R,N,V_connectionURL) connectionURL;
@property (Ti,R,N,V_interfaceIndex) interfaceIndex;
@property (T@"NSNumber",R,C,N,V_sendBufferSize) sendBufferSize;
@property (TB,R,N,V_wwanPreferred) wwanPreferred;
@property (T@"SNConnectionType",R,N,V_connectionType) connectionType;
@property (T@"NSString",C,N,V_policyId) policyId;
```

## Instance methods

```
-[SNConnectionAnalysisInfo setPolicyId:];
-[SNConnectionAnalysisInfo sendBufferSize];
-[SNConnectionAnalysisInfo connectionType];
-[SNConnectionAnalysisInfo interfaceIndex];
-[SNConnectionAnalysisInfo policyId];
-[SNConnectionAnalysisInfo connectionURL];
-[SNConnectionAnalysisInfo initWithConnectionURL:interfaceIndex:sendBufferSize:wwanPreferred:connectionType:policyId:];
-[SNConnectionAnalysisInfo wwanPreferred];
```
