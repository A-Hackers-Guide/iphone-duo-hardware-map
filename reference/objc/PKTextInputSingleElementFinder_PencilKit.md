# `PKTextInputSingleElementFinder`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKTextInputElementsFinder`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _finished;
@"PKTextInputElement" _foundElement;
@"NSSet" _candidateElements;
```

## Properties

```
@property (T@"PKTextInputElement",R,N,V_foundElement) foundElement;
@property (T@"NSSet",R,N,V_candidateElements) candidateElements;
@property (TB,R,N,GisFinished,V_finished) finished;
```

## Instance methods

```
-[PKTextInputSingleElementFinder isFinished];
-[PKTextInputSingleElementFinder _finishSingleElementSearchIfReadyAtPosition:coordinateSpace:candidates:completion:];
-[PKTextInputSingleElementFinder candidateElements];
-[PKTextInputSingleElementFinder findSingleElementAtPosition:coordinateSpace:completion:];
-[PKTextInputSingleElementFinder findSingleElementCloseToPosition:coordinateSpace:completion:];
-[PKTextInputSingleElementFinder foundElement];
```
