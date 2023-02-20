import random
import time

import os
from psychopy import core
from screeninfo import get_monitors
from Template_Task_Psychopy.task_template import TaskTemplate


class ChangeSignal(TaskTemplate):
    # IMPORTANT ! To MODIFY IF NEEDED
    bg = "white"
    text_color = "black"
    nb_ans = 2
    response_pad = False  # has to be set on "True" on production.
    eye_tracker_study = False  # same
    # END OF IMPORTANT
    yes_key_name = "verte"
    yes_key_code = "p"
    no_key_name = "rouge"
    no_key_code = "a"
    quit_code = "q"
    keys = ["space", yes_key_name, no_key_name, quit_code]
    launch_example = False
    trials = 400
    score = 0
    exp_start_timestamp = time.time()

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    #####################################
    ## METTRE LES CONSIGNES INES !!!!  ##
    #####################################
    instructions = [
        f"Dans cette expérience : \n\n - appuyez sur la touche {yes_key_name} pour selectionner la réponse "
        f"de droite. \n\n - appuyez sur la touche {no_key_name} pour selectionner la réponse de "
        f"gauche.",
        "N'appuyez sur les touches colorées que lorsque la question apparaît.",
        f"Placez vos index sur les touches {no_key_name} et {yes_key_name}."
    ]
    csv_headers = [
        "id_candidate",
        "no_trial",
        "ans_candidate",
        "good_ans",
        "result",
        "score",
        "reaction_time",
        "time_stamp",
    ]

    L = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 3, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 3, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 3, 1, 1, 0,
        0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 2, 1, 1, 0, 1, 1, 1, 0, 3, 0, 1, 0, 1, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 2, 1, 1,
        1, 0, 1, 1, 1, 3, 0, 0, 0, 1, 2, 1, 1, 0, 3, 0, 0, 1, 3, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 2, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 2, 1, 1, 0, 0, 0, 1, 0, 3, 2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 1, 0, 0,
        1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 3, 2, 3, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 3, 1, 0, 0, 1, 0, 3, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]

    def task(self, no_trial):
        self.create_visual_text("+", color=self.text_color).draw()
        self.win.flip()
        core.wait(0.5)
        waiting_time = 0.25
        if self.L[no_trial] == 0 or self.L[no_trial] == 1:
            self.create_visual_image(image=f"img/img_{self.L[no_trial]}.png", size=[get_monitors()[0].width, get_monitors()[0].height]).draw()
            self.win.flip()
            resp, rt = self.get_response_with_time(timeout=1)
            print("resp ==", resp)

        else:
            if self.L[no_trial] == 2:
                self.create_visual_image(image=f"carre.jpeg", pos=(-450, 0)).draw()
            else:
                self.create_visual_image(image=f"carre.jpeg", pos=(-450, 0)).draw()
            self.win.flip()
            core.wait(waiting_time)
            self.create_visual_image(image=f"img/img_{self.L[no_trial]}.png",
                                     size=[get_monitors()[0].width, get_monitors()[0].height]).draw()
            self.win.flip()
            resp, rt = self.get_response_with_time(timeout=1)
            print("resp ==", resp)

        if self.L[no_trial] == 0 or self.L[no_trial] == 3:
            good_ans = self.no_key_code
        else:
            good_ans = self.yes_key_code

        if resp == good_ans:
            if waiting_time >= 0.2:
                waiting_time -= 0.05
            self.score += 1
        else:
            waiting_time += 0.05

        self.update_csv(
            self.participant,
            no_trial,
            [resp if resp is not None else -1][0],
            good_ans,
            bool(resp == good_ans),
            self.score,
            [round(rt, 2) if rt is not None else -1][0],
            [round(time.time() - self.exp_start_timestamp, 2) if rt is not None else -1][0]
        )

        #            [round(rt, 2) if rt is not None else None],
        #    [round(time.time() - self.exp_start_timestamp, 2) if rt is not None else None],
        self.create_visual_text("").draw()
        self.win.flip()
        if no_trial == 99 or no_trial == 199 or no_trial == 299:
            self.create_visual_text("Pause de deux minutes !").draw()
            self.win.flip()
            core.wait(120)

        core.wait(3)


exp = ChangeSignal("csv")
exp.start()
