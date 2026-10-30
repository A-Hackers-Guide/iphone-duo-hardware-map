# `SBStateDumpService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemServiceServerStateDumpDelegate`
- 1 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"FBServiceClientAuthenticator" _clientAuthenticator;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStateDumpService init];
-[SBStateDumpService _authenticateClient:];
-[SBStateDumpService systemServiceServer:client:availableDomainsWithCompletion:];
-[SBStateDumpService systemServiceServer:client:disableRemoteStateDumpWithCompletion:];
-[SBStateDumpService systemServiceServer:client:disableRemoteStreamingWithCompletion:];
-[SBStateDumpService systemServiceServer:client:enableRemoteStateDumpWithTimeout:completion:];
-[SBStateDumpService systemServiceServer:client:enableRemoteStreamingWithTimeout:completion:];
-[SBStateDumpService systemServiceServer:client:lastEntriesForDomain:count:withCompletion:];
-[SBStateDumpService systemServiceServer:client:port:startStreamingStateDumpToFileForDomain:toFileAtPath:withCompletion:];
-[SBStateDumpService systemServiceServer:client:requestStateDump:toTextFileAtPath:];
-[SBStateDumpService systemServiceServer:client:requestStateDump:withCompletion:];
```
