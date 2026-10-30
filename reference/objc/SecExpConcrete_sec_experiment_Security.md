# `SecExpConcrete_sec_experiment`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_sec_experiment`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SecExperiment" innerExperiment;
Q numRuns;
Q successRuns;
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
-[SecExpConcrete_sec_experiment identifier];
-[SecExpConcrete_sec_experiment name];
-[SecExpConcrete_sec_experiment initWithName:];
-[SecExpConcrete_sec_experiment copyExperimentConfiguration];
-[SecExpConcrete_sec_experiment experimentIsAllowedForProcess];
-[SecExpConcrete_sec_experiment initWithInnerExperiment:];
-[SecExpConcrete_sec_experiment isSamplingDisabled];
-[SecExpConcrete_sec_experiment isSamplingDisabledWithDefault:];
```
