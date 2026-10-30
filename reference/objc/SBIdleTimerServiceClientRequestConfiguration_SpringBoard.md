# `SBIdleTimerServiceClientRequestConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
i _scenePID;
@"BSProcessHandle" _process;
@"ITIdleTimerConfiguration" _configuration;
```

## Properties

```
@property (Ti,R,N,V_scenePID) scenePID;
@property (T@"BSProcessHandle",R,N,V_process) process;
@property (T@"ITIdleTimerConfiguration",R,N,V_configuration) configuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerServiceClientRequestConfiguration succinctDescriptionBuilder];
-[SBIdleTimerServiceClientRequestConfiguration process];
-[SBIdleTimerServiceClientRequestConfiguration descriptionWithMultilinePrefix:];
-[SBIdleTimerServiceClientRequestConfiguration succinctDescription];
-[SBIdleTimerServiceClientRequestConfiguration configuration];
-[SBIdleTimerServiceClientRequestConfiguration description];
-[SBIdleTimerServiceClientRequestConfiguration descriptionBuilderWithMultilinePrefix:];
-[SBIdleTimerServiceClientRequestConfiguration initWithScenePID:process:configuration:];
-[SBIdleTimerServiceClientRequestConfiguration scenePID];
```
