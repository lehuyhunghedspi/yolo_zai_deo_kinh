from algorithm.architecture.model.yolo_try_1 import yolo

model_dict={
    'yolo_try_1':yolo
}

def get_model(name):
    return model_dict[name]()