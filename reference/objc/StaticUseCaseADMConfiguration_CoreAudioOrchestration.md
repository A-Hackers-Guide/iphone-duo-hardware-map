# `StaticUseCaseADMConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 admConfig;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 useCaseID;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 exclaveFormat;
```

## Properties

```
@property (T@"NSDictionary",N,R) negotiateDictionary;
@property (T@"NSDictionary",N,R) adaptDictionary;
@property (T@"NSArray",N,R) inputStreamIndicesInIOProc;
@property (T@"NSArray",N,R) outStreamIndicesInIOProc;
@property (T@"NSNumber",N,R) frameBufferSize;
@property (T@"ExclaveAudioFormatBase",N,R) exclaveAudioFormat;
```

## Instance methods

```
-[StaticUseCaseADMConfiguration init];
-[StaticUseCaseADMConfiguration initWithUseCaseID:];
-[StaticUseCaseADMConfiguration frameBufferSize];
-[StaticUseCaseADMConfiguration adaptDictionary];
-[StaticUseCaseADMConfiguration exclaveAudioFormat];
-[StaticUseCaseADMConfiguration initWithUseCaseID:andDeviceTreeInfo:];
-[StaticUseCaseADMConfiguration inputStreamIndicesInIOProc];
-[StaticUseCaseADMConfiguration negotiateDictionary];
-[StaticUseCaseADMConfiguration outStreamIndicesInIOProc];
```
