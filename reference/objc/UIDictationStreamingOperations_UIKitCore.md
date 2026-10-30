# `UIDictationStreamingOperations`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 21 instance methods, 0 class methods

## Instance variables

```
d _timeAfterInsertion;
d _timeAfterSelectRange;
@"<UITextInput>" _document;
@"NSMutableArray" _operations;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_operations) operations;
```

## Instance methods

```
-[UIDictationStreamingOperations pop];
-[UIDictationStreamingOperations init];
-[UIDictationStreamingOperations popAndInvoke];
-[UIDictationStreamingOperations setDocument:];
-[UIDictationStreamingOperations operations];
-[UIDictationStreamingOperations isEmpty];
-[UIDictationStreamingOperations isNotEmpty];
-[UIDictationStreamingOperations setOperations:];
-[UIDictationStreamingOperations clearOperations];
-[UIDictationStreamingOperations _performReplaceSelectedText:];
-[UIDictationStreamingOperations delayAfterSelector:];
-[UIDictationStreamingOperations dictationWillBeginInDocument:];
-[UIDictationStreamingOperations hasOperations];
-[UIDictationStreamingOperations performSelectRangeForSpeech:];
-[UIDictationStreamingOperations pushInsertTextForSpeech:];
-[UIDictationStreamingOperations pushReplaceSelectionWithText:];
-[UIDictationStreamingOperations pushSelectRangeForSpeech:];
-[UIDictationStreamingOperations pushSpeechOperation:];
-[UIDictationStreamingOperations pushSpeechOperationWithSelectionChangeDelta:block:];
-[UIDictationStreamingOperations selectionChangeDelta];
-[UIDictationStreamingOperations willEndEditingInInputDelegate:];
```
