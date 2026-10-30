# `NWCandidate`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NWConcrete_nw_candidate_manager" manager;
@"NSObject<OS_nw_interface_option_details>" details;
@"NSObject<OS_nw_path_evaluator>" evaluator;
@"NSObject<OS_nw_path>" current_path;
b1 original;
b1 ids;
b1 evaluating;
b1 submitted;
```

## Instance methods

```
-[NWCandidate dealloc];
-[NWCandidate redactedDescription];
-[NWCandidate description];
-[NWCandidate isEligible];
-[NWCandidate handleNewPath:];
-[NWCandidate initCandidate:forManager:evaluator:];
-[NWCandidate startEvaluator];
```
