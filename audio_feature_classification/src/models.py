from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier

def set_model(X_train, X_test, y_train, mode = 'rf'):

    y_pred = []
    print('Model starts training...')
    if mode == 'rf':
        clf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        clf = clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        return y_pred

    elif mode == 'sgd':
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        params = {
            'penalty': 'l2', 'l1_ratio': 0.2549999999999999,
            'class_weight': None, 'average': True, 'alpha': 0.010800000000000002
            }
        sgd_clf = SGDClassifier(**params, random_state=42,
                                max_iter=10, loss='log_loss', n_jobs=4, verbose=10)
        sgd_clf.fit(X_train_scaled, y_train)
        y_pred = sgd_clf.predict(X_test_scaled)

    elif mode == 'svc':
        clf = svm.SVC(decision_function_shape='ovo')
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

    else:
        print(" 'mode' option is to be in ['rf', 'sgd', 'mlp', 'svc'] ")

    return y_pred