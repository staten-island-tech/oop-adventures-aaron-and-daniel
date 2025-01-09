            if streak >= 5 and not power_up_used:
                use_power_up_button = Button(screen_width // 2 - 100, screen_height // 1.5, 250, 50, BLUE, "Use 50/50 Powerup")
                use_power_up_button.draw(screen)

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if use_power_up_button.is_clicked(mouse_pos, mouse_pressed):
                    power_up_used = True
                    correct_option = question.correct_answer
                    incorrect_options = [option for option in question.options if option != correct_option]
                    random.shuffle(incorrect_options)
                    question.options = [correct_option] + incorrect_options[:1]

            # Display answer choices
            buttons = []
            for i, option in enumerate(question.options):
                button = Button(100, 150 + i * 60, 600, 50, BLUE, option)
                buttons.append(button)
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            selected_wrong = False
            selected_correct = False
            selected_answer = ""

            for button in buttons:
                if button.is_clicked(mouse_pos, mouse_pressed):
                    selected_answer = button.text
                    if button.text == question.correct_answer:
                        score += 1
                        selected_correct = True
                        streak += 1  
                        if streak > highest_streak:  
                            highest_streak = streak
                    else:
                        selected_wrong = True
                        streak = 0  

            for button in buttons:
                if selected_answer == button.text:
                    if selected_correct:
                        button.draw(screen, GREEN)
                    elif selected_wrong:
                        button.draw(screen, RED)
                    else:
                        button.draw(screen)
                else:
                    button.draw(screen)

            if selected_wrong:
                game_over = True

            if selected_correct and not selected_wrong:
                pygame.time.wait(100)  
                current_question += 1
                if current_question >= len(questions):
                    game_over = True
            screen.blit(streak_image, (10, 10))  
            streak_text = font.render(f"Streak: {streak}", True, WHITE)
            screen.blit(streak_text, (60, 15)) 

            pygame.display.flip()

    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  
                pygame.quit()
                sys.exit()

run_trivia_game()