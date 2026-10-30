# `/usr/lib/libCRFSuite.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 428,336 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2288)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/usr/lib/libCRFSuite.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (365)

```
p < 0
addListNodeRanked
Macro-average precision, recall, F1: (%f, %f, %f)\n
Writing label features\n
gamma
_
calibration.max_trials
Error norm: %f\n
nSV = %d, nBSV = %d\n
%f
number of features = 
The threshold for the stopping criterion; an optimization process stops when\nthe improvement of the log likelihood over the last ${period} iterations is no\ngreater than this threshold.
calibration.samples: %d\n
averaging: %d\n
operator+
dictionary
variance
Trial #%d (eta = %f): 
stop: %d\n
svm_type %s\n
SV\n
feature.possible_states
.
Loss: %f\n
performing AGIS
period: %d\n
Check for the marginal probability (1,%d)-(2,%d)... 
operator-
type
one_class
classify
Stochastic Gradient Descent (SGD)\n
Calibrating the learning rate (eta)\n
model->quantized_header
l2sgd
int
Entry does not exist
efficient_maxent.cpp
calculating empirical expectation...
Improvement ratio: %f\n
linesearch.max_iterations: %d\n
Number of active features: %d (%d)\n
Warning: attributes will not be stored, because \"crfsuite_training_do_not_store_attributes\" is specified.\n
qmw_write_label_features
prod != 0
calibration.rate
StrongBacktracking
L-BFGS terminated with error code (%d)\n
Coefficient for L1 regularization.
OK (%f)\n
%Y-%m-%dT%H:%M:%SZ
averaging
nr_sv
unknown text in model file: [%s]\n
mathvec.h
wb
c
specified nu is infeasible
Number of features: %d\n
Total seconds required for training: %.3f\n
max_iterations
\n
train/
eta0 = 
_num_classes == (int)membp.size()
period
The number of limited memories for approximating the inverse hessian matrix.
The maximum number of trials for the line search algorithm.
c: %f\n
averaged-perceptron
unknown
calibration.candidates: %d\n
Line search step: %f\n
Model doesn't contain information for SVR probability inference\n
degree
BurstTrie.cpp
Error: missing label dictionary.\n
[UNKNOWN]
    %s: (%d, %d, %d) (******, ******, ******)\n
Operation successful
error: too much heldout data. no training data is available.
c1
epsilon_svr
c2: %f\n
Writing attribute feature counts and offsets.\n
UNKNOWN ERROR
probability != 0 and probability != 1
Check for the marginal probability (0,%d)-(1,%d)... 
feature.minfreq
destination <= 255
passive-aggressive
c2
%f (worse)\n
performing SGD
lCRF
rb
lbfgs
    %s: (%d, %d, %d) (%1.4f, %1.4f, %1.4f)\n
The initial variance of every feature weight.
The maximum number of trials of learning rates for calibration.
nu <= 0 or nu > 1
linear
  (%d) %s --> %s: %f\n
calibration.eta
kernel_type %s\n
Prob. model for test data: target value = predicted value + z,\nz: Laplace distribution e^(-|z|/sigma)/(2sigma),sigma= %g\n
Coefficient for L2 regularization.
feature.possible_states: %d\n
  type: %c%c%c%c\n
  off_features: 0x%X\n
SGD terminated with the maximum number of iterations\n
crf_paragraph_set_id
nu = %f\n
crf1d_model.c
L-BFGS terminated with the stopping criteria\n
Check for the sequence %d-%d-%d... 
Exceeds max_iter in multiclass_prob\n
  num_attrs: %d\n
%d
***** Epoch #%d *****\n
operator+=
 %d
nullptr == trie->mapbase
  off_labels: 0x%X\n
feature_counts[i] <= 255
Str
nr_class
Number of active labels: %d (%d)\n
feature->type == FT_TRANS
performing OWLQN
L-BFGS optimization\n
The aggressiveness parameter.
feature.possible_transitions: %d\n
  magic: %c%c%c%c\n
qmw_write_attribute_feature_counts_and_offsets
Averaged perceptron\n
The stopping criterion (the ratio of incorrect label predictions).
warning: class label %d specified in weight is not found\n
total_sv
one-class SVM probability output not supported yet
qmw_write_attribute_feature
crf1dm_initialize_state_scores_quantized
Feature
The maximum number of iterations (epochs) for SGD optimization.
SGD terminated with the stopping criteria\n
total_sv %d\n
degree of polynomial kernel < 0
sigmoid
Writing labels\n
basic_string
string
(int)_fb.Size() == x.size()
iter = %2d  C = %d  f = %10.7f  train_err = %7.5f
Learning rate (eta): %f\n
shrinking != 0 and shrinking != 1
Check for the partition factor... 
Writing feature references for transitions\n
a.Size() == b.Size()
delta
Force to generate possible state features.
Instance accuracy: %d / %d (%1.4f)\n
epsilon
num_memories
levels.size() <= keyLen + 1
Check for the marginal probability (2,%d)... 
  size: %d\n
Terminated with the stopping criterion\n
calibration.candidates
0:%d 
C = %f\n
reverseBurst
The minimum frequency of features.
Number of active attributes: %d (%d)\n
model->compact_header
arow
probA
addListNode
crf1d_encode.c
vector
max_iterations: %d\n
The duration of iterations to test the stopping criterion.
Total number of feature updates: %.0f\n
max_linesearch
serializeLevels
  heldout_logl(err) = %f (%6.4f)
 alpha = 
Storing the model\n
id >= 0 && id < (int)id2mef.size()
Insufficient memory to complete operation
delta: %f\n
linesearch: %s\n
c_svc
advanceMapCursorTrieList
}\n
cmw_write_attribute_feature
conditional_probability
number of samples = 
error_sensitive: %d\n
nr_class %d\n
 \t
cache_size <= 0
FAIL: %f (%f)\n
error: L2 regularization is currently not supported in SGD mode.
epsilon: %f\n
Backtracking
Passive Aggressive\n
unknown svm type
C <= 0
listcount <= trie->reserved[ContainerSize]
ERROR: overflow loss\n
error_sensitive
%d:%.8g 
items.size() < sizeThreshold
r
float
variance: %f\n
The stopping criterion (the mean loss).
id >= 0 && id < (int)id2str.size()
The number of candidates of learning rate.
CQDB
%3d  obj(err) = %f (%6.4f)
LABELS = {\n
gamma: %f\n
Line search trials: %d\n
crf_paragraph_get_id
l >= 0 && l <= MAX_LABEL_TYPES
The maximum number of iterations for L-BFGS optimization.
%.16g 
coef0
TRANSITIONS = {\n
Item accuracy: %d / %d (%1.4f)\n
done
type: %d\n
probB
bitcount == count
burstTrieCreateCursorWithTrieLevelRef
Error: missing attribute dictionary.\n
Holdout group: %d\n
num_classes() == (int)membp.size()
num_memories: %d\n
  num_features: %d\n
Entry already exists
\t
  off_attrs: 0x%X\n
Invalid argument to function
C = 
warning: _num_class != _label_bag.Size()
L2 regularizer = 
Feature L2-norm: %f\n
MoreThuente
%80s
crf1de_write_external_attribute_model
fwrite(&feature, 1, sizeof(compact_attribute_feature_t), concrete_writer->fp) == sizeof(compact_attribute_feature_t)
Performance by label (#match, #model, #ref) (precision, recall, F1):\n
error: could not write out features!
linesearch
The strategy for updating feature weights: {\n    0: PA without slack variables,\n    1: PA type I,\n    2: PA type II\n}.\n
degree %d\n
nu_svc
Writing attributes\n
Adaptive Regularization of Weights (AROW)\n
error: L1 and L2 regularizers cannot be used simultaneously.
The initial value of learning rate (eta) used for calibration.
The number of instances used for calibration.
index >= 0
gamma %g\n
nu_svr
Number of active label features: %d\n
performing LBFGS
preparing for estimation...
number of active features = 
error: cannot open 
!
b.Size() == _v.size()
Consider the number of incorrect labels to the cost function.
Number of labels: %d\n
STATE_FEATURES = {\n
fwrite(&feature, 1, sizeof(quantized_attribute_feature_t), concrete_writer->fp) == sizeof(quantized_attribute_feature_t)
Feature norm: %f\n
error: too many types of labels.
coef0 %g\n
label
svm_type
 
Initial loss: %f\n
kernel_type
unknown kernel function.\n
%lf
SV
traverseFromMapCursorTrieList
cursor.prfxlen <= head->restlen
ME_Feature
ERROR: \"crfsuite_training_do_not_store_attributes\" flag is not compatible with minimal frequency value that is greater than 1!\n
Check for the marginal probability (0,%d)... 
feature.minfreq: %f\n
ATTRIBUTES = {\n
FunctionGradient
L-BFGS terminated with the maximum number of iterations\n
backward_compatibility.c
Writing feature references for attributes\n
%f\n
w
polynomial
type: CRF1d\n
FILEHEADER = {\n
No more entries in range
Tradeoff parameter.
Check for the marginal probability (1,%d)... 
feature.possible_transitions
calibration.rate: %f\n
The threshold for the stopping criterion; an L-BFGS iteration stops when the\nimprovement of the log likelihood over the last ${period} iterations is no\ngreater than this threshold.
rho
serializeLevelsRanked
Force to generate possible transition features.
0
precomputed
  off_labelrefs: 0x%X\n
Best learning rate (eta): %f\n
gamma < 0
epsilon = %f\n
Feature generation\n
Writing attribute features.\n
The rate of increase/decrease of learning rate for calibration.
calibration.max_trials: %d\n
Epsilon for testing the convergence of the objective.
obj = %f, rho = %f\n
Reaching maximal iterations in two-class probability estimates\n
cursor->prfxlen <= head->restlen
The maximum number of iterations.
index >= 0 && index < paragraph->num_items*paragraph->num_attrs
\nWarning: using -h 0 may be faster\n
Total nSV = %d\n
eps <= 0
  %5d: %s\n
crf1dm_initialize_state_scores_compact
efficient_maxent.h
error: no training data.
calibration.samples
calibration.eta: %f\n
c1: %f\n
The line search algorithm used in L-BFGS updates:\n{   'MoreThuente': More and Thuente's method,\n    'Backtracking': Backtracking method with regular Wolfe condition,\n    'StrongBacktracking': Backtracking method with strong Wolfe conditi
Seconds required: %.3f\n
To use compact or quantized format, you must store attributes and labels out side of crfsuite model.\n
  num_labels: %d\n
  off_attrrefs: 0x%X\n
***** Iteration #%d *****\n
L1 regularizer = 
f >= 0 && f <= 0xffffff
Active features: %d\n
  version: %d\n
num_labels <= 255
crf1d/
Compute the average of feature weights (similarly to Averaged Perceptron).
unknown svm type.\n
Line search fails in two-class probability estimates\n
rbf
Number of attributes: %d\n
Number of active attribute features: %d\n
L-BFGS resulted in convergence\n
*
\noptimization finished, #iter = %d\n
 %g
:
unknown kernel type
Seconds required for this iteration: %.3f\n
```
