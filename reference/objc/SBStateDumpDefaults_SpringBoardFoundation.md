# `SBStateDumpDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 8 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TB,D,N,GisRemoteDumpEnabled) remoteDumpEnabled;
@property (TB,D,N,GisRemoteStreamEnabled) remoteStreamEnabled;
@property (T@"NSArray",&,N) tempFileWritePolicy;
@property (T@"NSNumber",&,D,N) tempFileMaxSizeBytes;
@property (T@"NSNumber",&,D,N) tempFileMaxAgeSeconds;
@property (TB,D,N) tempFileDeleteOnReboot;
@property (Td,D,N) remoteDumpTimeoutExpiry;
@property (Td,D,N) remoteStreamTimeoutExpiry;
```

## Instance methods

```
-[SBStateDumpDefaults _bindAndRegisterDefaults];
-[SBStateDumpDefaults setTempFileWritePolicy:];
-[SBStateDumpDefaults tempFileWritePolicy];
```
